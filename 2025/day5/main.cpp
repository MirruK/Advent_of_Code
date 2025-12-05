#include <iostream>
#include <string>
#include <vector>
#include <optional>

using Range = std::pair<long, long>;

Range record_range(std::string s){
  long fst = std::stol(s.substr(0,s.find("-")));
  long snd = std::stol(s.substr(s.find("-")+1,s.length()));
  return {fst,snd};
}

// Trim overlapping ranges before inserting


long sum_range(Range r) {
  long a0 = r.first;
  long s1 = (a0*(a0+1)) / 2;
  long a1 = r.second;
  long s2 = (a1*(a1+1)) / 2;
  return s2 - s1;
}

bool in_range(Range r, long val){
  return val >= r.first && val <= r.second;
}

bool ranges_overlap(Range r1, Range r2){
  if (r1.second < r2.first && r1.first > r2.second ) return false;
  return true;
}

std::optional<Range> merge_ranges (Range r1, Range r2){
  bool o = ranges_overlap(r1,r2);
  if (!o) {
    return std::nullopt;
  }
  if (o && r1.first <= r2.first && r2.second >= r1.second) 
    return std::optional<Range>{{r1.first, r2.second}};
  if(o && r2.first <= r1.first && r1.second >= r2.second)
    return std::optional<Range>{{r2.first, r1.second}};
  if (o && r1.first <= r2.first && r1.second >= r2.second)
    return r1;
  return r2;
}

std::vector<Range> merge_all_ranges(std::vector<Range> rs){
  std::vector<Range> new_rs;
  int merged = 1;
  while (merged){
    rs = new_rs;
    new_rs = {};
    merged = 0;
  for(int i = 1; i < rs.size(); i++){
    auto mr = merge_ranges(rs[i-1], rs[i]);
    if (mr.has_value()) {
      new_rs.push_back(mr.value());
      merged++;
    }
    else{new_rs.push_back(rs[i-1]);}
  }
  }
  return rs;
}

bool any(const std::vector<Range>& rs, long val){
  for(const auto& r: rs){
    if (in_range(r, val)) {
      return true;
    }
  }
  return false;
}

int main(){
  int part = 0;
  std::vector<long> ids;
  std::vector<Range> ranges;
  for(std::string line; std::getline(std::cin, line);){
    if(line == ""){
      part = 1;
      continue;
    }
    if (part == 0){
      ranges.push_back(record_range(line));
    }
    else{
      ids.push_back(std::stol(line));
    }
  }
  int sum1 = 0;
  long long sum2 = 0;
  for(const auto& id: ids){
    if (any(ranges, id)) {
      sum1++;
    }
  }
  for(auto r: ranges){
    sum2 += (long long)sum_range(r);
  }
  auto rs = merge_all_ranges(ranges);
  std::cout << "Part 1: " << sum1 << std::endl;
  std::cout << "Part 2: " << rs.size() << std::endl;
}

