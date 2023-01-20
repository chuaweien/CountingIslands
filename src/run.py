from typing import List
import sys

from src.validate import validate_inputs


class IslandsCounting:

    def dfs(self, grid: List[int], x: int, y: int) -> None:
        """Using DFS to find all the "1" in the same island

        :param List grid: input grid
        :param int x: x coordinate
        :param int y: y coordinate
        """
        stack = [(x, y)]

        while stack:
            x, y = stack.pop()
            grid[x] = grid[x][:y] + "/" + grid[x][y+1:]
            search_x = [x+1, x-1, x]
            search_y = [y+1, y-1, y]

            # list all the 8 possible directions:
            # (x-1, y+1)        (x, y+1)      (x+1, y+1)
            # (x-1, y)          (x, y)        (x+1, y)
            # (x-1, y-1)        (x, y-1)      (x+1, y-1)

            dirs = [(i, j) for i in search_x for j in search_y]

            for i, j in dirs:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                    stack.append((i, j))

    def read_input_file(self, input_filepath: str) -> List[str]:
        with open(input_filepath, "r") as f:
            grid = [line.strip() for line in f.readlines()]

        return grid

    def count_islands(self, grid: List[str]) -> int:
        """Count number of islands in input file using Depth First Search (DFS).

        :param str input_filepath: input filepath to .txt file
        :return int: number of islands
        """
        # if input is empty file
        if len(grid) == 0:
            raise ValueError("Input is empty!")

        # validate inputs before proceeding
        validate_inputs(grid)

        islands_count = 0
        visited = [[False for _ in range(len(grid[0]))]
                   for _ in range(len(grid))]

        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if grid[x][y] == "1":
                    self.dfs(grid, x, y)
                    islands_count += 1

        return islands_count


if __name__ == "__main__":
    islands = IslandsCounting()
    grid = islands.read_input_file(sys.argv[1])
    print(islands.count_islands(grid))
