#include <iostream>
#include <string>
#include <vector>

int remove_rolls(std::vector<char> &pre, std::vector<char> &post, int m, int n,
                 int offset) {
  m -= offset;
  n -= offset;
  int roll_count = 0;
  int accessible_rolls = 0;
  for (int row = offset; row < m; row++) {
    for (int col = offset; col < n; col++) {
      roll_count = 0;
      if (pre[row * n + col] == '.')
        continue;
      for (int k = 0; k < 9; k++) {
        int tile_col = (k % 3) - 1;
        int tile_row = (k / 3) - 1;
        int absolute_idx = (row + tile_row) * n + (col + tile_col);
        // Skip counting the roll we are on right now
        if (tile_col == 0 && tile_row == 0)
          continue;
        if (row + tile_row < m && row + tile_row >= 0 && col + tile_col < n &&
            col + tile_col >= 0 && pre[absolute_idx] == '@') {
          // Pad room with empty space
          roll_count++;
        }
      }
      if (roll_count < 4) {
        accessible_rolls++;
        post[row * n + col] = '.';
      }
    }
  }
  return accessible_rolls;
}

bool check_outer_empty(const std::vector<char> &room, int m, int n,
                       int offset) {
  m -= offset;
  n -= offset;
  int abs_idx_s = 0;
  int abs_idx_e = 0;
  for (int col = offset; col < n; col++) {
    abs_idx_s = (0 * (n)) + col;
    abs_idx_e = (m - 1) * (n) + col;
    if (room[abs_idx_s] == '@' || room[abs_idx_e] == '@')
      return false;
  }
  for (int row = 0; row < m; row++) {
    abs_idx_s = row * n + 0;
    abs_idx_e = row * n + (n - 1);
    if (room[abs_idx_s] == '@' || room[abs_idx_e] == '@')
      return false;
  }
  return true;
}

int main() {
  std::vector<char> room;

  int rows = 0;
  int cols = 0;
  for (std::string line; std::getline(std::cin, line);) {
    for (char c : line) {

      room.push_back(c);
    }
    // std::cout << line << std::endl;
    rows++;
    cols = line.size();
  }
  int accessible = 1;
  int sum = 0;
  int offset = 0;
  std::vector<char> room_after = room;
  while (accessible > 0) {
    accessible = remove_rolls(room, room_after, rows, cols, offset);
    sum += accessible;
    // make sure this is a deep copy
    room = room_after;
    if (check_outer_empty(room, rows, cols, offset)) {
      offset++;
    }
  }
  std::cout << "Accessible rolls: " << sum << std::endl;
}
