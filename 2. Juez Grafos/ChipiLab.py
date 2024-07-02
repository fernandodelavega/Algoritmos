from collections import deque

def is_valid_move(grid, visited, x, y, turn):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False
    if grid[x][y] == -1 and turn % 2 != 1:
        return False
    if visited[x][y] != -1:
        return False
    return True

def find_minimum_distance(grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = len(grid)
    m = len(grid[0])
    visited = [[-1] * m for _ in range(n)]
    queue = deque([(0, 0, 1)])  # (x, y, turn)
    visited[0][0] = 1

    while queue:
        x, y, turn = queue.popleft()

        if grid[x][y] == 2:
            return visited[x][y] - 1

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(grid, visited, new_x, new_y, turn):
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append((new_x, new_y, turn + 1))

    return -1  # No se encontró un camino al maletín

# Lectura de la entrada
N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# Resolución y salida
print(find_minimum_distance(grid))
