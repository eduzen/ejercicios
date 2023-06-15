try:
    from rich import print
except ImportError:
    pass

from collections import deque
from copy import deepcopy


def print_grid(grid: list[list[int]]) -> None:
    print("Grid:")
    for row in grid:
        print(row)
    print("-")
    print()


def is_last_postion(len_of_rows: int, len_of_columns: int, position_row: int, postion_col: int) -> bool:
    # If I reach the len of rows or columns, that means that
    # I have reached the end of the grid
    if (position_row == (len_of_rows - 1)) and (postion_col == (len_of_columns - 1)):
        return True
    return False


def is_reachable(grid: list[list[int]]) -> bool:
    len_of_rows = len(grid)    # number of rows
    len_of_columns = len(grid[0]) # number of columns

    if len_of_rows == 1 and len_of_columns == 1:
        return grid[0][0] == 0

    # Create a queue and add the start position to it
    queue = deque([(0, 0)])

    # Define the directions for right and down
    DIRECTIONS = tuple([(0, 1), (1, 0)])

    # Create a copy of the grid to mark visited cells
    visited_grid = deepcopy(grid)


    while queue:
        position_row, postion_col = queue.popleft()

        if is_last_postion(len_of_rows, len_of_columns, position_row, postion_col):
            return True

        for step_forward, step_down in DIRECTIONS:
            next_row = position_row + step_forward
            next_col = postion_col + step_down

            inside_row = 0 <= next_row < len_of_rows
            inside_col = 0 <= next_col < len_of_columns

            if not (inside_row and inside_col):
                continue

            print(f"next_row: {next_row}, next_col: {next_col} value: {visited_grid[next_row][next_col]}")

            empty = visited_grid[next_row][next_col] == 0

            if empty:
                # Mark as visited by setting to 'x' in the copy
                visited_grid[next_row][next_col] = 'x'
                queue.append((next_row, next_col))

            # print_grid(visited_grid)


def main() -> None:
    # Test
    grid = [[0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 0, 0]]

    print_grid(grid)
    print("-" * 10)

    print(is_reachable(grid))  # Should print True


if __name__ == "__main__":
    main()
