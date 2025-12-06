#include <cctype>
#include <iterator>
#include <map>
#include <optional>
#include <string>
#include <iostream>
#include <variant>
#include <vector>

int add(int a, int b) {
  return a + b;
}

int mul(int a, int b) {
  return a * b;
}
static int(*ops_bucket[2])(int, int) = {&add, &mul};

std::optional<int> consume_int(std::string::iterator& s, std::string::iterator end) {
  std::string buf;
  while(s != end && !std::isspace(*s)){
    buf.push_back(*s);
    s = std::next(s);
  }
  if (buf.length() < 1) {
    return {};
  }
  return std::stoi(buf);
}

int main(){
  std::optional<int> n;
  std::map<int, std::vector<int>> num_buckets;
  std::vector<bool> op_buckets;
  int i = 0;
  for (std::string line; std::getline(std::cin, line); i++) {
    if (line.find("+") != std::string::npos || line.find("*") != std::string::npos) {
      for (auto it = line.begin(); it != line.end(); it++) {
        if(*it == '+'){
          op_buckets.push_back(false);
        }
        if(*it == '*'){
          op_buckets.push_back(true);

        }
        
      }
    }
    auto it = line.begin();
    auto end = line.end();
    while((n = consume_int(it, end)).has_value()){
      if (num_buckets.find(i ) == num_buckets.end()) {
        num_buckets.insert({i, std::vector<int> {n.value()}});
      }
      else{
        num_buckets[i].push_back(n.value());
      }
    }
  }
}


