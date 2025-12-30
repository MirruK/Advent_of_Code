#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <map>

using Pos = std::pair<long, long>;
using Rect = std::pair<Pos,Pos>;


std::string repr_rect(Rect r) {
  return std::format("{{{},{}}}, {{{},{}}}", r.first.first, r.first.second, r.second.first, r.second.second);
}

long area(const Pos& p0, const Pos& p1){
  return ((std::abs(p0.first-p1.first)+1)*
		(std::abs(p0.second-p1.second)+1));
}

struct RectLess {
    bool operator()(const Rect& a, const Rect& b) const {
        return area(a.first, a.second) < area(b.first, b.second);
    }
};

Pos parse_range(std::string s){
  auto sep = s.find(",");
  auto fst = s.substr(0, sep);
  auto snd = s.substr(sep+1, s.length() - (sep+1));
  return {std::stol(fst), std::stol(snd)};
}

std::map<Rect, long, RectLess> permute(const std::vector<Pos>& vec){
  std::map<Rect, long, RectLess> areas;
  for(int i = 0; i < vec.size(); i++){
    for(int j = i+1; j < vec.size(); j++){
      auto fst = vec[i];
      auto snd = vec[j];
      areas.insert({{fst, snd},area(fst,snd)});
    }
  }
  return areas;
}

bool inside_rect(const Pos& p, const Rect& r){
  long v1x;
  long v1y; 
  long v2x; 
  long v2y; 
  if(r.first.first < r.second.first) {
    v1x = r.first.first;
    v2x = r.second.first;
  }
  else{
    v1x = r.second.first;
    v2x = r.first.first;
  }
  if(r.first.second < r.second.second){
    v1y = r.first.second;
    v2y = r.second.second;
  }else {
    v1y = r.second.second;
    v2y = r.first.second;
  }
  auto px = p.first;
  auto py = p.second;
  if ((px > v1x)&& (px < v2x) && (py > v1y) && (py < v2y)){
    return false;
  }
  return true;
}

bool is_valid_rect(const Rect& r, const std::vector<Pos>& ps){
  for(const auto& p: ps){
    if(inside_rect(p,r)){
      return false;
    }
  }
  return true;
}

std::map<Rect, long, RectLess> find_valid_areas(const std::vector<Pos>& vec){
  std::map<Rect, long, RectLess> areas;
  for(int i = 0; i < vec.size(); i++){
    for(int j = i+1; j < vec.size(); j++){
      auto fst = vec[i];
      auto snd = vec[j];
      auto r = Rect{fst, snd};
      if(is_valid_rect(r, vec)){
	areas.insert({{fst, snd},area(fst,snd)});	
      }
    }
  }
  return areas;
}



int main(){
  std::vector<Pos> rs;
  for(std::string line; std::getline(std::cin, line); ){
    rs.push_back(parse_range(line));
  }
  auto areas = permute(rs);
  auto valid_areas = find_valid_areas(rs);
  
  std::cout << "part1: " << areas.rbegin()->second  << std::endl;
  for(auto v: valid_areas){
    std::cout << "v2: " << v.second << std::endl;
  }
  //std::cout << "part2: " << valid_areas.rbegin()->second  << std::endl;
  
  return 0;
}
