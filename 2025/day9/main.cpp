#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <map>

using Pos = std::pair<long, long>;
using Range = std::pair<long, long>;
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

std::vector<Rect> connect_lines(const std::vector<Pos>& vec){
  std::vector<Rect> lines;
  Pos snd;
  for(int i = 1; i <= vec.size(); i++){
    auto fst = vec[i-1];
    if(i == vec.size()){
      snd = vec[0];
    }else {
      snd = vec[i];
    }
    lines.push_back(Rect{fst, snd});
  }
  return lines;
}

bool inside(Range r1, Range r2){
  if (r1 < r2) return r1.second > r2.first;
  else return r2.second > r1.first;
}

Range new_range(long f, long s) {
  if (f <= s) return {f, s};
  else return {s, f};
  // auto smaller = f <= s ? f : s;
  // auto larger = f > s ? f : s;
  // return {smaller,larger};
}

bool inside_rect(const Rect& l, const Rect& r){
  // Run with optimization flags and this horribly slow code
  // gets optimized away
  Range CDx = new_range(l.first.first, l.second.first);
  Range CDy = new_range(l.first.second, l.second.second);
  Range ABx = new_range(r.first.first, r.second.first);
  Range ABy = new_range(r.first.second, r.second.second);
  return inside(CDx, ABx) && inside(CDy, ABy);
}

bool is_valid_rect(const Rect& r, const std::vector<Rect>& lines){
  for(const auto& l: lines){
    if(inside_rect(l,r)){
      return false;
    }
  }
  return true;
}

std::map<Rect, long, RectLess> find_valid_areas(const std::vector<Pos>& vec, const std::vector<Rect>& lines){
  std::map<Rect, long, RectLess> areas;
  for(int i = 0; i < vec.size(); i++){
    for(int j = i+1; j < vec.size(); j++){
      auto fst = vec[i];
      auto snd = vec[j];
      auto r = Rect{fst, snd};
      if(is_valid_rect(r, lines)){
	areas.insert({r,area(fst,snd)});
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
  auto lines = connect_lines(rs);
  auto valid_areas = find_valid_areas(rs, lines);
  
  std::cout << "part1: " << areas.rbegin()->second  << std::endl;
  std::cout << "part2: " << valid_areas.rbegin()->second  << std::endl;
  
  return 0;
}
