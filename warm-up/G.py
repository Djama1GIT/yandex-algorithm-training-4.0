N, M = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(N))


def max_carrot_square(grid):
    # Create a copy of the grid to avoid modifying the original
    grid = [row[:] for row in grid]
    max_side = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if i > 0 and j > 0:
                    # Update the cell value to be the minimum of its top, left, and top-left neighbors, plus one
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1]) + 1
                # Update the maximum side length
                max_side = max(max_side, grid[i][j])

    return max_side


print(max_carrot_square(matrix))
