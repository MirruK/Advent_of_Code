#include <string>
#include <unordered_set>
#include <iostream>
#include <vector>
#include <map>

using Pos = std::pair<int,int>;

namespace std {
struct hash_pair {
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2>& p) const
    {
        // Hash the first element
        size_t hash1 = hash<T1>{}(p.first);
        // Hash the second element
        size_t hash2 = hash<T2>{}(p.second);
        // Combine the two hash values
        return hash1
               ^ (hash2 + 0x9e3779b9 + (hash1 << 6)
                  + (hash1 >> 2));
    }
};
}

/*
std::vector<int> find_all(std::string s, char c){
  int p = 0;
  int sz = s.length();
  std::vector<int> ps;
  while((p = s.find(c)) != string::npos) {
    s = s.substr(p, s.size()-p);
    ps.push_back((sz -  s.length()) + p);
  }
  return ps;
}
*/

long simulate_timelines(const std::vector<std::string>& lines, int row, int col, int bound){
  static std::map<std::pair<long, long> ,long> cache;
  if (cache.find({row,col}) != cache.end()) {
    return cache[{row,col}];
  }
  long value = 0;
    if(row == 0) {
      if(lines[0][col] == 'S') return 1;
      else return 0;
    }
    if (lines[row-1][col] == '^') {
      return 0;
    }
    if(col > 0 && lines[row][col-1] == '^'){
      value += simulate_timelines(lines, row-1, col-1, bound);
    }
    if(col < bound - 1 && lines[row][col+1] == '^') value += simulate_timelines(lines, row-1, col+1, bound);
    value += simulate_timelines(lines, row-1, col, bound);
    cache[{row,col}] = value;
    return value;
}

int simulate(std::unordered_set<Pos, std::hash_pair>& lasers, std::string line){
  std::vector<Pos> snapshot(lasers.begin(), lasers.end());
  int count = 0;
  for(auto l: snapshot){
    auto col = l.second;
    if(line[col] == '^') {
      count++;
      lasers.erase(l);
      Pos left_laser = {l.first+1, l.second-1};
      Pos right_laser = {l.first+1, l.second+1};
      lasers.insert(left_laser);
      lasers.insert(right_laser);
    } else {
      lasers.erase(l);
      lasers.insert({l.first+1, l.second});
    }
  }
  return count;
}

int count_splits(const std::vector<std::string>& lines){
  int split_count = 0;
  // Positions stored in row-major order
  std::unordered_set<Pos, std::hash_pair> lasers = {{1,lines[0].find("S")}};
  for(int i = 1; i < lines.size(); i++){
    split_count+= simulate(lasers, lines[i]);
  }
  return split_count;
}


int main(){
  std::vector<std::string> lines;
  for(std::string line; std::getline(std::cin, line);){
    lines.push_back(line);
    //std::cout << "line: " << line << std::endl;
  }
  long sum = 0;
  for(int i = 0; i < lines[0].length(); i++){
    sum += simulate_timelines(lines, lines.size()-1, i, lines[0].length());
  }
  std::cout << "part1: " << count_splits(lines) << std::endl;
  std::cout << "part2: " << sum << std::endl;
}
