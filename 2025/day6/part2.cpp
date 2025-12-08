#include <cctype>
#include <iterator>
#include <map>
#include <optional>
#include <string>
#include <iostream>
#include <variant>
#include <vector>


long long operate_on_columns(std::vector<std::string>& lines, int start_col, int col_count, char op){
  std::string n;
  long long total = op == '+' ? 0 : 1;
    long long num;  
    // For col_start, col_count columns forward
  for(int col = start_col; col < start_col + col_count; col++){
      // For every row
    for(auto& line : lines){
      // as int
      // long num = line[col]-'0';
      if (!isspace(line[col]))
      n.push_back(line[col]);
    }

    if (op == '+'){
      num = n.length() > 0 ? std::stoll(n) : 0;
      total += num;
    } else {
      num = n.length() > 0 ? std::stoll(n) : 1;
      total *= num;
    }
    n = "";
    num = 0;
  }
  return total;
}

int main(){
  std::optional<long long> n;
  std::map<int, std::vector<long long>> num_buckets;
  std::vector<short> op_buckets;
  int col = 0;
  std::vector<std::string> lines;
  for (std::string line; std::getline(std::cin, line);) {
    lines.push_back(line);
  }
  int max = 0;
  for (int i = 0; i < lines.size(); i++) {
    if (lines[i].size() >= max) {
      max = lines[i].size();
    }
  }
  for(auto& line : lines){
    line.resize(max, ' ');
  }
  auto ops = lines.back();
  lines.pop_back();
  std::vector<int> col_sizes;
  std::vector<int> operators;
  int curr = 0;
  char curr_op = ops[0];
  int total = 0;
  for (auto c : ops){
    if ((!isspace(c) && curr != 0) || (total == (ops.size() - 1))){
      if(total == (ops.size() - 1)) {
	col_sizes.push_back(curr+1);
      }else{
      col_sizes.push_back(curr);
      }
      operators.push_back(curr_op);
      curr_op = c;
      curr = 0;
    }
    curr++;
    total++;
  }
  for(auto cs : col_sizes) {
    std::cout << cs << std::endl;
  }
  // col_sizes[col_sizes.size()-1]++;
  col = 0;
  long long sum = 0;
  for(int i = 0; i < col_sizes.size(); i++){
    sum += operate_on_columns(lines, col, col_sizes[i], operators[i]);
    col+=col_sizes[i];
  }
  std::cout << "Sum part2: " << sum << std::endl;

}
