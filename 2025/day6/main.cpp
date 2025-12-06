#include <cctype>
#include <iterator>
#include <map>
#include <optional>
#include <string>
#include <iostream>
#include <variant>
#include <vector>


long long dispatch_fn(const std::vector<long long>& is, int op){
  long long sum = 0;
  long long product = 1;
  for(auto v: is){
    if (op == 0) {
      sum += v;
    } else {
      product *= v;
    }
  }
  return op == 0 ? sum : product;
}

std::optional<long long> consume_int(std::string::iterator& s, std::string::iterator end) {
  std::string buf;
  while(std::isspace(*s)){s = std::next(s);}
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
  std::optional<long long> n;
  std::map<int, std::vector<long long>> num_buckets;
  // std::map<int, std::vector<long long>> num_buckets2;
  std::vector<short> op_buckets;
  int col = 0;
  for (std::string line; std::getline(std::cin, line);) {
    if (line.find("+") != std::string::npos || line.find("*") != std::string::npos) {
      for (auto it = line.begin(); it != line.end(); it++) {
        if(*it == '+'){
          op_buckets.push_back(0);
	  col++;
        }
        if(*it == '*'){
          op_buckets.push_back(1);
	  col++;
        }
      }
      col = 0;
      break;
    }
    auto it = line.begin();
    auto end = line.end();
    while((n = consume_int(it, end)).has_value()){
      if (num_buckets.find(col) == num_buckets.end()) {
        num_buckets.insert({col, std::vector<long long> {n.value()}});
      }
      else{
        num_buckets[col].push_back(n.value());
      }
      col++;
    }
    col = 0;
  }
  long long sum1 = 0;
  for(int i = 0; i < op_buckets.size(); i++){
    sum1 += dispatch_fn(num_buckets[i], op_buckets[i]);
  }
  std::cout << "Sum 1: " << sum1 << std::endl;
}
