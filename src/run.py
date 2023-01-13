from typing import List
import sys

from validate import validate_inputs


def dfs(lines: List, x: int, y: int) -> None:
    if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[x]) or lines[x][y] != "1":
        return

    # replace the element "1" to "/" to mark that it is already counted
    if lines[x][y] == "1":
        lines[x] = lines[x][:y] + "/" + lines[x][y+1:]

    search_x = [x+1, x-1, x]
    search_y = [y+1, y-1, y]

    # list all the possible directions:
    # (x-1, y+1)        (x, y+1)      (x+1, y+1)
    # (x-1, y)          (x, y)        (x+1, y)
    # (x-1, y-1)        (x, y-1)      (x+1, y-1)

    dirs = [(i, j) for i in search_x for j in search_y]

    for dir in dirs:
        dfs(lines, dir[0], dir[1])


def count_islands(input_filepath: str) -> int:
    """Count number of islands in input file using Depth First Search.

    :param str input_filepath: input filepath to .txt file
    :return int: number of islands
    """

    with open(input_filepath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    if len(lines) == 0:
        return "Input is empty!"

     # validate inputs before proceeding
    validate_inputs(lines)

    islands_count = 0

    for x, row in enumerate(lines):
        for y, col in enumerate(row):
            if lines[x][y] == "1":
                dfs(lines, x, y)
                islands_count += 1

    return islands_count


if __name__ == "__main__":
    print(count_islands(sys.argv[1]))
