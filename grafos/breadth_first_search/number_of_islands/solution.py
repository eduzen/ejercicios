from collections import deque

def is_valid_and_unvisited(
    grid: list[list[str]], visited: set[tuple[int, int]], row: int, col: int
) -> bool:
    within_grid = row in range(len(grid)) and col in range(len(grid[0]))
    if not within_grid:
        return False

    unvisited = (row, col) not in visited
    is_land = grid[row][col] == "1"

    if is_land and unvisited:
        return True
    return False


def bfs(
    grid: list[list[str]], visited: set[tuple[int, int]], row: int, col: int
) -> None:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque()
    visited.add((row, col))
    queue.append((row, col))

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if is_valid_and_unvisited(grid, visited, new_r, new_c):
                queue.append((new_r, new_c))
                visited.add((new_r, new_c))


def number_of_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if is_valid_and_unvisited(grid, visited, r, c):
                bfs(grid, visited, r, c)
                islands += 1

    return islands



def main() -> None:
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    islands = number_of_islands(grid)
    print(f"Number of islands: {islands}")
    print(islands == 1)


if __name__ == "__main__":
    main()
