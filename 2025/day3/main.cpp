#include <string>
#include <ranges>
#include <cctype>
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using ValWithIdx = std::pair<int, int>;

long largest_non_consecutive_num(std::vector<int> xs, int n){
  // 1. iterate from back, record largest element and index
  // 1.5. if index of largest > xs.size() - digits left
  // then pick another
  // 2 xs = xs[maxIdx:]
  // Repeat until n numbers found
  int bound = -1;
  std::vector<ValWithIdx> largest;
  for (int i = 0; i<n; i++){
    largest.push_back({INT_MIN,0});
  }
  for(int pass = n; pass>0; pass--){
    for(int r = xs.size()-pass; r>bound; r--){
      if (xs[r] >= largest[largest.size() - pass].first) {
	if (pass != n && largest[largest.size() - pass].second == r){
	  continue;
	}
	largest[largest.size() - pass] = {xs[r], r};
      }
    }
    bound = largest[largest.size() - pass].second;
  }
  auto result = std::ranges::fold_left(
      largest | std::views::transform([](auto& k) {return std::to_string(k.first);}),
      std::string(""),
      std::plus<>());
  return std::stol(result);
}

int main (){
  std::vector<std::vector<int>> banks;
  long sum1 = 0;
  long sum2 = 0;
  for (std::string line; std::getline(std::cin, line);) {
    auto result = line
      | std::views::transform([](char c) { return int(c-'0'); })
      | std::ranges::to<std::vector<int>>();
    banks.push_back(std::move(result));
  }
  for (auto b : banks) {
    sum1 += largest_non_consecutive_num(b, 2);
    sum2 += largest_non_consecutive_num(b, 12);
  }
  std::cout << sum1 << std::endl;
  std::cout << sum2 << std::endl;
}
