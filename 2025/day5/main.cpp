#include <algorithm>
#include <iostream>
#include <optional>
#include <string>
#include <vector>

using Range = std::pair<long, long>;

Range record_range(std::string s) {
  long fst = std::stol(s.substr(0, s.find("-")));
  long snd = std::stol(s.substr(s.find("-") + 1, s.length()));
  return {fst, snd};
}

long long count_range(Range r) { return (r.second - r.first) + 1; }

bool in_range(Range r, long val) { return val >= r.first && val <= r.second; }

bool ranges_overlap(Range r1, Range r2) {
  if (r1.second < r2.first)
    return false;
  return true;
}

std::optional<Range> merge_ranges(Range r1, Range r2) {
  bool o = ranges_overlap(r1, r2);
  if (!o) {
    return std::nullopt;
  }
  long bigger2 = r1.second > r2.second ? r1.second : r2.second;
  return Range{r1.first, bigger2};
}

void merge_all_ranges(std::vector<Range> &rs) {
  int merged = 1;
  while (merged) {
    merged = 0;
    for (int i = 1; i < rs.size(); i++) {
      auto mr = merge_ranges(rs[i - 1], rs[i]);
      if (mr.has_value()) {
        rs[i] = mr.value();
        rs.erase(rs.begin() + i - 1);
        i--;
        merged++;
      }
    }
  }
}

bool any(const std::vector<Range> &rs, long val) {
  for (const auto &r : rs) {
    if (in_range(r, val)) {
      return true;
    }
  }
  return false;
}

int main() {
  int part = 0;
  std::vector<long> ids;
  std::vector<Range> ranges;
  for (std::string line; std::getline(std::cin, line);) {
    if (line == "") {
      part = 1;
      continue;
    }
    if (part == 0) {
      ranges.push_back(record_range(line));
    } else {
      ids.push_back(std::stol(line));
    }
  }
  int sum1 = 0;
  long long sum2 = 0;
  for (const auto &id : ids) {
    if (any(ranges, id)) {
      sum1++;
    }
  }
  std::sort(ranges.begin(), ranges.end());
  merge_all_ranges(ranges);

  for (auto r : ranges) {
    sum2 += (long long)count_range(r);
  }
  std::cout << "Part 1: " << sum1 << std::endl;
  std::cout << "Part 2: " << sum2 << std::endl;
}
