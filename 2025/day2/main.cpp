#include <iostream>
#include <vector>

typedef struct {
  long s;
  long e;
} Range;

Range from_str(const std::string s) {
  long i = s.find("-");
  auto f = std::stol(s.substr(0, i));
  auto l = std::stol(s.substr(i + 1, s.length()));
  return Range{f, l};
}

bool has_repeated_nums(long i) {
  auto str = std::to_string(i);
  auto len = str.length();
  if (len % 2 != 0)
    return false;
  auto fst = str.substr(0, len / 2);
  auto snd = str.substr(len / 2, len);
  return fst == snd;
}

bool has_repeated_nums2(long i) {
  auto str = std::to_string(i);
  auto len = str.length();
  if (len == 1)
    return false;
  for (int n = 1; n < len / 2 + 1; n++) {
    int partitions = len / n;
    auto partition = str.substr(0, n);
    bool rolling_res = true;
    for (int ps = n; ps + n <= len; ps += n) {
      rolling_res = (str.substr(ps, n) == partition) && rolling_res;
      if ((len - (ps + n)) < partition.length() && (len - (ps + n)) > 0)
        rolling_res = false;
      if (!rolling_res)
        break;
    }
    if (rolling_res)
      return true;
  }
  return false;
}

int main() {
  std::string line;
  std::getline(std::cin, line);
  long pos = 0;
  std::string token;
  std::vector<Range> rs;
  std::vector<long> nums;
  std::string delimiter = ",";
  while ((pos = line.find(delimiter)) != std::string::npos) {
    token = line.substr(0, pos);
    line.erase(0, pos + delimiter.length());
    rs.push_back(from_str(token));
  }
  rs.push_back(from_str(line));
  long sum = 0;
  long sum2 = 0;
  for (auto r : rs) {
    for (long i = r.s; i <= r.e; i++) {
      if (has_repeated_nums(i)) {
        nums.push_back(i);
        sum += i;
      }
      if (has_repeated_nums2(i)) {
        sum2 += i;
      }
    }
  }
  std::cout << "Sum: " << sum << std::endl;
  std::cout << "Sum part 2: " << sum2 << std::endl;
}
