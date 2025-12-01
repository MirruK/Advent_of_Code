#include <cstdio>
#include <iostream>
#include <string>

static int zero_count = 0;
static int zero_count2 = 0;

int solve(int start, int dir, int amount) {
  start = (start + (amount * dir)) % 100;
  if (start == 0)
    zero_count += 1;
  return start;
}

int sgn(int val) { return val >= 0 ? 1 : -1; }

int solve2(int start, int dir, int amount) {
  int n = (start + (amount * dir));
  int div = n / 100;
  int mod = n > -1 ? n % 100 : 100 - (std::abs(n) % 100);
  if (mod == 100)
    mod = 0;
  // std::cout << "Rotated to: " << mod << '\n';
  if (n == 0) {
    zero_count2++;
    return mod;
  }
  if (sgn(start) != sgn(n) && n != 0 && start != 0) {
    zero_count2 += std::abs(div) + 1;
    return mod;
  }
  zero_count2 += std::abs(div);
  return mod;
}

int main() {
  int dir;
  int amount;
  int curr = 50;
  for (std::string line; std::getline(std::cin, line);) {
    // std::cout << line << std::endl;
    dir = line.substr(0, 1) == "L" ? -1 : 1;
    auto s_it = line.begin();
    std::advance(s_it, 1);
    std::string amount_s = "";
    for (auto it = s_it; it != line.end(); it++) {
      if (!std::isdigit(*it))
        break;
      amount_s.push_back(*it);
    }
    amount = std::stoi(amount_s);
    // curr = solve(curr, dir, amount);
    curr = solve2(curr, dir, amount);
  }
  std::cout << zero_count << '\n';
  std::cout << zero_count2 << '\n';
  return 0;
}
