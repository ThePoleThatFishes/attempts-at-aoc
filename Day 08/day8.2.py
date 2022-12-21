import numpy as np

with open("day8_input.txt", "r") as f:
    grid = []
    for line in f:
        add_line = line.strip()
        grid.append([int(char) for char in add_line])

    grid = np.array(grid)
    scenic = 0
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            complete = [False, False, False, False]
            num_checks = 0
            scene = [0, 0, 0, 0]
            while sum(complete) != 4:
                num_checks += 1
                if not complete[0]:  # northern check
                    scene[0] += 1
                    if j - num_checks == 0 or grid[i, j] <= grid[i, j - num_checks]:
                        complete[0] = True

                if not complete[1]:  # southern check
                    scene[1] += 1
                    if j + num_checks == 98 or grid[i, j] <= grid[i, j + num_checks]:
                        complete[1] = True

                if not complete[2]:  # western check
                    scene[2] += 1
                    if i - num_checks == 0 or grid[i, j] <= grid[i - num_checks, j]:
                        complete[2] = True

                if not complete[3]:  # western check
                    scene[3] += 1
                    if i + num_checks == 98 or grid[i, j] <= grid[i + num_checks, j]:
                        complete[3] = True

            scenic = max(scenic, scene[0] * scene[1] * scene[2] * scene[3])
    print(scenic)
