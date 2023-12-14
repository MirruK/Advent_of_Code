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

/* Expands universe according to the rules of Advent of Code
   mutating the galaxy map in the process */
struct galaxy_map expand_universe(struct galaxy_map map) {
  int *cols_to_expand = calloc(map.width, sizeof(int));
  int *rows_to_expand = calloc(map.height, sizeof(int));
  size_t num_rows_to_add = 0;
  size_t num_columns_to_add = 0;
  // 1. Count columns without any galaxies & store the indexes for the columns
  int matched_row = -1, matched_column = -1;
  int end;
  for (int i = 0; i < map.width; i++) {
    end = (map.width * map.height - (map.width - i)) + 1;
    matched_column = str_search('#', map.flat_map, i, end, map.width);
    if (matched_column == -1) {
      cols_to_expand[i] = 1;
      num_columns_to_add++;
    }
  }
  // 2. The same as above but for rows.
  for (int i = 0; i < map.height; i++) {
    matched_row = str_search('#', map.flat_map, i * map.width,
                             i * map.width + map.width, 1);
    if (matched_row == -1) {
      rows_to_expand[i] = 1;
      num_rows_to_add++;
    }
  }
  // 3. Allocate new resized array of empty space and recreate the map
  size_t new_width = num_columns_to_add + map.width;
  size_t new_height = num_rows_to_add + map.height;
  size_t new_map_size = new_width * new_height;
  assert(new_map_size > 0);
  char *new_map = malloc(new_map_size);
  size_t new_map_idx = 0;
  for (size_t i = 0; i < map.height * map.width;) {
    if (rows_to_expand[i / map.height] == 1) {
      for (size_t j = 0; j < new_width * 2; j++) {
        new_map[new_map_idx++] = map.flat_map[i];
      }
      i += map.width;
    } else if (cols_to_expand[i % map.width] == 1) {
      new_map[new_map_idx++] = map.flat_map[i];
      new_map[new_map_idx++] = map.flat_map[i++];
    } else {
      new_map[new_map_idx++] = map.flat_map[i++];
    }
  }
  struct galaxy_map new_map_struct = {
      .flat_map = new_map, .width = new_width, .height = new_height};
  free(cols_to_expand);
  free(rows_to_expand);
  cols_to_expand = NULL;
  rows_to_expand = NULL;
  return new_map_struct;
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
  // printf("%s\n", flat_map);
  struct galaxy_map map = {
      .flat_map = flat_map, .width = width, .height = height};
  return map;
}

void compute_galaxy_distances(struct galaxy_map universe,
                              size_t number_of_galaxies,
                              int *galaxy_locations) {
  int count = 0;
  int sum = 0;
  for (size_t i = 0; i < number_of_galaxies; i++) {
    for (size_t j = i + 1; j < number_of_galaxies; j++) {
      int g_pos1 = galaxy_locations[i];
      int g_row1 = (g_pos1 / (int)universe.width);
      int g_col1 = (g_pos1 % (int)universe.width);
      int g_pos2 = galaxy_locations[j];
      int g_row2 = (g_pos2 / (int)universe.width);
      int g_col2 = (g_pos2 % (int)universe.width);
      int manhattan_distance = abs(g_row1 - g_row2) + abs(g_col1 - g_col2);
      // printf("Galaxy 1: (%d, %d)\n", g_row1, g_col1);
      // printf("Galaxy 2: (%d, %d)\n", g_row2, g_col2);
      // printf("Manhattan distance: %d\n", manhattan_distance);
      count++;
      sum += manhattan_distance;
    }
  }
  printf("Sum of distances: %d\n", sum);
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
  struct galaxy_map expanded_universe = expand_universe(universe);
  printf("%s\n", expanded_universe.flat_map);
  printf("Expanded width: %zd\n", expanded_universe.width);
  printf("Expanded height: %zd\n", expanded_universe.height);
  int *matches =
      malloc(sizeof(int) * expanded_universe.height * expanded_universe.width);
  size_t matches_len;
  matches_len = str_search_all(
      '#', expanded_universe.flat_map,
      expanded_universe.height * expanded_universe.width, 0, matches);
  compute_galaxy_distances(expanded_universe, matches_len, matches);
  free(expanded_universe.flat_map);
  free(universe.flat_map);
  free(matches);
  return 0;
}