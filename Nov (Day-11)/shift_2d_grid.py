def shiftGrid(grid, k):
    m = len(grid)
    n = len(grid[0])
    total = m * n
    flat = []
    for row in grid:
        for value in row:
            flat.append(value)
    shifted = [0] * total
    for i in range(total):
        new_index = (i + k) % total
        shifted[new_index] = flat[i]
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(shifted[i * n + j])
        result.append(row)
    return result
m = int(input())
n = int(input())
grid = []
for i in range(m):
    row = list(map(int, input().split()))
    grid.append(row)
k = int(input())
print(shiftGrid(grid, k))
