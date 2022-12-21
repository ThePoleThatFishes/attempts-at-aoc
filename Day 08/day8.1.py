import numpy as np

with open("day8_input.txt", "r") as f:
    grid = []
    for line in f:
        add_line = line.strip()
        grid.append([int(char) for char in add_line])

    grid = np.array(grid)
    visible = 4 * (grid.shape[0] - 1)
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            if (grid[i, j] > (grid[i, 0:j]).max() or grid[i, j] > (grid[i+1: grid.shape[0], j]).max()
            or grid[i, j] > (grid[i, j+1:grid.shape[1]]).max() or grid[i, j] > (grid[0:i, j]).max()):
                visible += 1

    print(visible)
