from typing import List
import sys


def validate_rows(arr: List) -> None:
    """Ensure that each row in array has same number of elements.
    If array is asymmetrical, it will output an error with row index.

    :param List arr: input 2D array
    :return None: None
    """
    n_elements = len(arr[0])

    for x, row in enumerate(arr):
        assert len(row) == n_elements, "Row {} is not symmetrical!".format(x)


def validate_ascii(arr: List) -> None:
    for x, row in enumerate(arr):
        assert all(ord(
            element) < 128 for element in row), "Row {} contains non-ascii characters".format(x)


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

     # validate that each row has same number of columns
    validate_rows(lines)
    validate_ascii(lines)

    islands_count = 0

    for x, row in enumerate(lines):
        for y, col in enumerate(row):
            if lines[x][y] == "1":
                dfs(lines, x, y)
                islands_count += 1

    return islands_count


if __name__ == "__main__":
    print(count_islands(sys.argv[1]))
