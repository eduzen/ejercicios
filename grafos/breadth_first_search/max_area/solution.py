from collections import deque


def is_valid(grid, visited,x, y):
    inside_x = 0 <= x < len(grid)
    if not inside_x:
        return False

    inside_y = 0 <= y < len(grid[0])
    if not inside_y:
        return False

    if (x, y) in visited:
        return False

    island = grid[x][y] == 1
    return island

def bfs(grid, visited, x, y):
    directions = (
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1)
    )
    queue = deque()
    queue.append((x, y))
    visited.add((x, y))
    area = 0

    while queue:
        row, col = queue.popleft()

        for next_x, next_y in directions:
            nx, ny = row + next_x, col + next_y
            if is_valid(grid, visited, nx, ny):
                area += 1
    return area


def main():
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0],
    ]

    len_x = len(grid)
    len_y = len(grid[0])

    area = 0
    visited = set()

    for x in range(len_x):
        for y in range(len_y):
            if is_valid(grid, visited, x, y):
                new_area = bfs(grid, visited, x, y)
                if new_area > area:
                    area = new_area

    print(area)
    print(area == 6)

if __name__ == '__main__':
    main()





