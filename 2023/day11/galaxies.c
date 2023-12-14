#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct galaxy_map {
  char *flat_map;
  size_t width;
  size_t height;
};

typedef struct sized_arr {
  int *arr;
  size_t len;
} sized_arr;

typedef struct vec2 {
  int row;
  int col;
} vec2;

/* Strips last newline from string and updates line_size to reflect the change.
  line_size is a pointer to the number of characters in the string (excluding
  null-byte)
 */
void strip_newline(char *linep, size_t *line_len) {
  if (*line_len < 1) {
    return;
  }
  if (linep[*line_len - 1] == '\n') {
    linep[*line_len - 1] = '\0';
    *line_len -= 1;
    return;
  }
  return;
}

/* Search "haystack" for "needle" starting from index "start" until index "end",
 * incrementing index by "step" each iteration, returning index where needle is
 found or -1 if no match was found */
int str_search(char needle, char *haystack, size_t start, size_t end,
               size_t step) {
  char c;
  int i = start;
  while (i < end && (c = haystack[i]) != '\0') {
    if (c == needle) {
      return i;
    }
    i += step;
  }
  return -1;
}

size_t str_search_all(char needle, char *haystack, size_t n, size_t start,
                      int *matches) {
  int ret = start - 1;
  size_t matches_len = 0;
  while ((ret = str_search(needle, haystack, ret + 1, n, 1)) > -1) {
    if (matches_len > n) {
      return matches_len;
    }
    matches[matches_len++] = ret;
  }
  return matches_len;
}

vec2 flat_to_2d_coord(int coord, size_t width) {
  int row = (coord / (int)width);
  int col = (coord % (int)width);
  vec2 ret = {.row = row, .col = col};
  return ret;
}

void find_expanded_regions(struct galaxy_map map, sized_arr *exp_rows,
                           sized_arr *exp_cols) {
  int *expanded_row_pos = calloc(map.height, sizeof(int));
  int *expanded_col_pos = calloc(map.width, sizeof(int));
  size_t num_rows_to_add = 0;
  size_t num_columns_to_add = 0;
  // 1. Count columns without any galaxies & store the indexes for the columns
  int matched_row = -1, matched_column = -1;
  int end;
  for (int i = 0; i < map.width; i++) {
    end = (map.width * map.height - (map.width - i)) + 1;
    matched_column = str_search('#', map.flat_map, i, end, map.width);
    if (matched_column == -1) {
      expanded_col_pos[num_columns_to_add++] = i;
    }
  }
  // 2. The same as above but for rows.
  for (int i = 0; i < map.height; i++) {
    matched_row = str_search('#', map.flat_map, i * map.width,
                             i * map.width + map.width, 1);
    if (matched_row == -1) {
      expanded_row_pos[num_rows_to_add++] = i;
    }
  }
  exp_cols->arr = expanded_col_pos;
  exp_cols->len = num_columns_to_add;
  exp_rows->arr = expanded_row_pos;
  exp_rows->len = num_rows_to_add;
}

/* Read an input file into a flat array
along with the width and height of the map*/
struct galaxy_map parse_input() {
  size_t line_size, line_len;
  size_t width = 0, height = 0, map_len = 0;

  char *linep = NULL;
  char *flat_map = malloc(1);

  while ((line_len = getline(&linep, &line_size, stdin)) != -1) {
    // 1. Strip newline
    strip_newline(linep, &line_len);
    // 2. Update map_len && realloc flat_map to fit new line
    map_len += line_size;
    flat_map = realloc(flat_map, map_len);
    if (flat_map == NULL) {
      perror("realloc() error: \n");
      exit(1);
    }
    // 3. Concatenate flat_map with linep
    strncat(flat_map, linep, line_size);
    // 4. Increment height && set width
    width = line_len;
    height++;
    // 5. free unneeded buffer alloced by getline
    free(linep);
    linep = NULL;
  }
  struct galaxy_map map = {
      .flat_map = flat_map, .width = width, .height = height};
  return map;
}

int expanded_regions_crossed(sized_arr expanded_rows, sized_arr expanded_cols,
                             vec2 galaxy1, vec2 galaxy2) {
  int regions_crossed = 0;
  for (int i = 0; i < expanded_rows.len; i++) {
    if ((expanded_rows.arr[i] > galaxy1.row &&
         expanded_rows.arr[i] < galaxy2.row) ||
        (expanded_rows.arr[i] < galaxy1.row &&
         expanded_rows.arr[i] > galaxy2.row)) {
      regions_crossed++;
    }
  }
  for (int i = 0; i < expanded_cols.len; i++) {
    if ((expanded_cols.arr[i] > galaxy1.col &&
         expanded_cols.arr[i] < galaxy2.col) ||
        (expanded_cols.arr[i] < galaxy1.col &&
         expanded_cols.arr[i] > galaxy2.col)) {
      regions_crossed++;
    }
  }
  return regions_crossed;
}

void compute_galaxy_distances(struct galaxy_map universe,
                              sized_arr galaxy_locations,
                              sized_arr expanded_rows, sized_arr expanded_cols,
                              int expansion_factor) {
  long sum = 0;
  for (size_t i = 0; i < galaxy_locations.len; i++) {
    for (size_t j = i + 1; j < galaxy_locations.len; j++) {
      vec2 g_pos1 = flat_to_2d_coord(galaxy_locations.arr[i], universe.width);
      vec2 g_pos2 = flat_to_2d_coord(galaxy_locations.arr[j], universe.width);
      int exp_regions_crossed = expanded_regions_crossed(
          expanded_rows, expanded_cols, g_pos1, g_pos2);
      int manhattan_distance =
          abs(g_pos1.row - g_pos2.row) + abs(g_pos1.col - g_pos2.col) +
          exp_regions_crossed * expansion_factor - exp_regions_crossed;
      sum += manhattan_distance;
    }
  }
  printf("Sum of distances: %ld\n", sum);
}

void test_str_search() {
  char *buf = "...#..a.";
  char needle = 'a';
  printf("Searching string: %s for %c\n", buf, needle);
  int ret = str_search(needle, buf, 0, 1000, 3);
  printf("Result should be positive, result: %d\n", ret);
}

void print_map(struct galaxy_map map) {
  for (size_t i = 0; i < map.height; i++) {
    for (size_t j = 0; j < map.width; j++) {
      printf("%c", map.flat_map[(i * map.width) + j]);
    }
    printf("\n");
  }
}

int main() {
  struct galaxy_map universe = parse_input();

  int *matches = malloc(sizeof(int) * universe.height * universe.width);
  size_t matches_len;
  matches_len = str_search_all('#', universe.flat_map,
                               universe.height * universe.width, 0, matches);
  sized_arr matches_sized = {.arr = matches, .len = matches_len};

  sized_arr exp_rows = {.arr = NULL, .len = 0};
  sized_arr exp_cols = {.arr = NULL, .len = 0};
  find_expanded_regions(universe, &exp_rows, &exp_cols);

  printf("Part 1:\n");
  compute_galaxy_distances(universe, matches_sized, exp_rows, exp_cols, 2);

  printf("Part 2:\n");
  compute_galaxy_distances(universe, matches_sized, exp_rows, exp_cols,
                           1000000);

  free(exp_rows.arr);
  free(exp_cols.arr);
  free(universe.flat_map);
  free(matches);
  return 0;
}