# O(N * M) time
# O(N * M) space

from typing import List, Set, Tuple

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Define the boundaries of the grid
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])

        # Create a set to keep track of visited coordinates
        visited_coordinates = set()

        def depth_first_search(row: int, column: int) -> int:
            # Check if the current coordinate is out of grid boundaries
            if row < 0 or row == number_of_rows or column < 0 or column == number_of_columns:
                return 0

            # Check if the current coordinate is water or has been visited
            if grid[row][column] == 0 or (row, column) in visited_coordinates:
                return 0

            # Mark the current coordinate as visited
            visited_coordinates.add((row, column))

            # Explore the surrounding coordinates: up, down, left, right
            return (1
                + depth_first_search(row + 1, column)
                + depth_first_search(row - 1, column)
                + depth_first_search(row, column + 1)
                + depth_first_search(row, column - 1)
            )

        max_area = 0
        # Iterate over the entire grid
        for row in range(number_of_rows):
            for column in range(number_of_columns):
                # Keep track of the maximum area of an island found so far
                max_area = max(max_area, depth_first_search(row, column))

        return max_area
