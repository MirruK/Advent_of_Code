#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <map>
#include <optional>


typedef struct {
  long x, y, z;
} Vec3;

struct Vec3Hash {
    std::size_t operator()(const Vec3& v) const noexcept {
        std::size_t h1 = std::hash<long>()(v.x);
        std::size_t h2 = std::hash<long>()(v.y);
        std::size_t h3 = std::hash<long>()(v.z);
        // combine hashes
        return h1 ^ (h2 << 1) ^ (h3 << 2);
    }
};

float dist(Vec3 x0, Vec3 x1) {
  return std::sqrt(std::pow(x1.x - x0.x, 2) +
		   std::pow(x1.y - x0.y, 2) +
		   std::pow(x1.z - x0.z, 2));
}

std::string repr_vec3(Vec3 v){
  return std::format("x: {}, y:{}, z:{}", v.x, v.y, v.z);
}

bool operator==(const Vec3& t, const Vec3 &o) {
        return t.x == o.x && t.y == o.y && t.z == o.z;
}


class UnionFind {
  public:
    std::unordered_map<Vec3, std::vector<Vec3>, Vec3Hash> representatives;
    UnionFind(const std::vector<Vec3>& vs) {
      representatives = {};
      for (auto v : vs) {
        representatives[v] = {};
      }
    }
    /* Finds which Vec3 is the representative for the category containing target*/
    Vec3 uf_find(Vec3 target) {
      if(representatives.find(target) != representatives.end())
        return target;   
      for (auto it = representatives.begin(); it != representatives.end(); it++) {
        for (auto& p : it->second) {
          if (target == p) {
            return it->first;
          }
        }
      }
      representatives[target] = {};
      return target;
    }
  std::pair<Vec3,Vec3> uf_union(Vec3 v1, Vec3 v2) {
      auto v3 = this->uf_find(v1);
      auto v4 = this->uf_find(v2);
      // The elements are already in the same set
      if (v3 == v4) return {v1,v2};
      auto &vec1 = representatives[v3];
      auto &vec2 = representatives[v4];
      vec1.push_back(v4);
      vec1.insert(vec1.end(), vec2.begin(), vec2.end());
      representatives.erase(v4);
      return {v1,v2};
    }
  std::vector<long> sizes(){
    std::vector<long> out;
    for(auto it = representatives.begin(); it != representatives.end(); it++){
      out.push_back(it->second.size());
    }
    return out;
  }
    void print() {
      for (auto it = this->representatives.begin(); it != this->representatives.end(); it++) {
        std::cout << std::format("representative: {}, set size: {}\n",repr_vec3(it->first), it->second.size());
      }
    }
};

 bool operator<(const std::pair<Vec3, Vec3>& p0, const std::pair<Vec3, Vec3>& p1){
   return dist(p0.first, p0.second) < dist(p1.first, p1.second);
 }

void permute(std::vector<Vec3> coords, std::map<std::pair<Vec3, Vec3>, float>& permutations) {
  for(int i = 0; i < coords.size(); i++){
    for(int j = i; j < coords.size(); j++){
      if (i == j) continue;
      Vec3 x0 = coords[i];
      Vec3 x1 = coords[j];
      permutations.insert({{x0, x1}, dist(x0,x1)});
    }
  }
}

std::optional<long> consume_num(std::string::iterator& it, std::string::iterator end) {
  std::string num;
  while(it != end && !isdigit(*it)) {
    it = std::next(it);
  }
  while(it != end && isdigit(*it)) {
    num.push_back(*it);
    it = std::next(it);
  }
  if (num.length() > 0) return std::stol(num);
  return std::nullopt;
}

int main(){
  std::optional<long> n = 0;
  std::vector<Vec3> points; 
  Vec3 curr = {0,0,0};
  int f = 0;
  for (std::string line; std::getline(std::cin, line);) {
    auto it = line.begin();
    auto ed = line.end();
    while((n = consume_num(it, ed)).has_value()){
      if (f==0){
	curr.x = n.value();
      } else if(f==1){
	curr.y = n.value();
      } else {
	curr.z = n.value();
      }
      f++;
    }
    if (f != 3) {
      std::cout << "We got a problem!" << std::endl;
    }

    points.push_back(curr);
    f = 0;
  }
  //auto ps = std::vector<Vec3>{{1,2,3},{4,2,8},{1,1,1},{8,3,5}};
  auto uf = UnionFind(points);
  std::map<std::pair<Vec3,Vec3>, float> distances;
  permute(points, distances);
  //for(auto it = distances.begin(); it != distances.end(); it++){
  //  std::cout << std::format("v1: {}, v2: {} => {}",repr_vec3(it->first.first), repr_vec3(it->first.second), it->second) << std::endl;
  //}
  //uf.print();
  long count = 0;
  std::pair<Vec3,Vec3> prevs = {{0,0,0},{0,0,0}};
  for (auto it = distances.begin(); it != distances.end(); it++) {
    if (uf.representatives.size() == 1){
      break;
    }
    prevs = uf.uf_union(it->first.first, it->first.second);
    count++;
  }
  // uf.print();
  std::cout << "v1: " << repr_vec3(prevs.first) << std::endl;
  std::cout << "v2: " << repr_vec3(prevs.second) << std::endl;
  auto szs = uf.sizes();
  std::sort(szs.begin(), szs.end());
  count = 0;
  long product = 1;
  for(auto it = szs.rbegin(); it != szs.rend() && count < 3; it++){
    // std::cout << "product: " << product << std::endl;
    // std::cout << "*it: " << *it << std::endl;
    product *= (*it) + 1;
    count++;
  }
  std::cout << "part1: " << product << std::endl;
  std::cout << "part2: " << prevs.first.x*prevs.second.x << std::endl;
}
