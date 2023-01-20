from typing import List
import sys

from src.validate import validate_inputs


class IslandsCounting:

    def dfs(self, grid: List[str], x: int, y: int) -> None:
        """Using Depth First Search (DFS) to find all the "1" in the same island by checking all 
           the possible 8 directions. Does not return any output but mutates the input grid by 
           replacing the found "1"s with "/"s to mark that it has been visited.

        :param List[str] grid: List of strings containing "1"s and "0"s to represent the input grid
        :param int x: An integer representing the x-coordinate of the starting point in the grid i.e. row
        :param int y: An integer representing the y-coordinate of the starting point in the grid i.e. column
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
                # for each direction if element is "1", coordinates are added to stack
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                    stack.append((i, j))

    def read_input_file(self, input_filepath: str) -> List[str]:
        """Reads the input from a file and returns a list of strings, 
           where each string represents a row of the grid.

        :param str input_filepath: A string representing the filepath of the input file.
        :return List[str]: List of strings containing "1"s and "0"s to represent the input grid
        """
        with open(input_filepath, "r") as f:
            grid = [line.strip() for line in f.readlines()]

        return grid

    def count_islands(self, grid: List[str]) -> int:
        """Counts the number of islands present in a 2D grid represented as a list of strings using
           DFS. The function first checks if the input is empty, if it is then it raises a 
           ValueError. It also validates the input by calling the `validate_input` function.

        :param List[str] grid: A list of strings representing the input grid, where each string 
                               represents a row of the grid containing "1"s and "0"s
        :raises ValueError: Input is empty
        :return int: Final count of islands
        """
        # if input is empty file
        if len(grid) == 0:
            raise ValueError("Input is empty!")

        # validate inputs before proceeding
        validate_inputs(grid)

        islands_count = 0

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
