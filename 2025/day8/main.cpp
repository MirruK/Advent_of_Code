#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <optional>

typedef struct {
  int x, y, z;
} Vec3;

bool operator==(const Vec3 &o) {
        return x == o.x && y == o.y && z == o.;
}

bool operator<(const Vec3 &o){
        return x < o.x || (x == o.x && y < o.y);
  }




std::string repr_vec3(Vec3 v){
  return std::format("x: {}, y:{}, z:{}\n", v.x, v.y, v.z);
}

float dist(Vec3 x0, Vec3 x1) {
  return std::sqrt(std::pow(x1.x - x0.x, 2) +
		   std::pow(x1.y - x0.y, 2) +
		   std::pow(x1.z - x0.z, 2));
}

void permute(std::vector<Vec3> coords, std::unordered_map<std::pair<Vec3, Vec3>, float>& permutations) {
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
  for (auto p : points) {
    std::cout << repr_vec3(p) << std::endl;
  }
  std::unordered_map<std::pair<Vec3,Vec3>, float> distances;
  permute(points, distances);
  for (auto it = distances.begin(); it != distances.end(); it++) {
    std::cout << std::format("v0: {}, v1: {} => dist: {}\n",repr_vec3(it->first.first), repr_vec3(it->first.second), it->second);
  }
}
