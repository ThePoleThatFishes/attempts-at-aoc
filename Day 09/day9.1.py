with open("day9_input.txt", "r") as f:
    grid = []
    for line in f:
        row = []
        line = line.strip("\n")
        for char in line:
            row.append(int(char))

        grid.append(row)

    risk_value = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if (i, j) == (0, 0):
                if grid[i][j] < min(grid[i][j+1], grid[i+1][j]):
                    risk_value += grid[i][j] + 1
            elif (i, j) == (len(grid) - 1, 0):
                if grid[i][j] < min(grid[i][j+1], grid[i-1][j]):
                    risk_value += grid[i][j] + 1
            elif (i, j) == (0, len(grid[i]) - 1):
                if grid[i][j] < min(grid[i][j-1], grid[i+1][j]):
                    risk_value += grid[i][j] + 1
            elif (i, j) == (len(grid) - 1, len(grid[i]) - 1):
                if grid[i][j] < min(grid[i][j-1], grid[i-1][j]):
                    risk_value += grid[i][j] + 1
            elif i == 0:
                if grid[i][j] < min(grid[i+1][j], grid[i][j-1], grid[i][j+1]):
                    risk_value += grid[i][j] + 1
            elif i == len(grid) - 1:
                if grid[i][j] < min(grid[i-1][j], grid[i][j-1], grid[i][j+1]):
                    risk_value += grid[i][j] + 1
            elif j == 0:
                if grid[i][j] < min(grid[i][j+1], grid[i-1][j], grid[i+1][j]):
                    risk_value += grid[i][j] + 1
            elif j == len(grid[i]) - 1:
                if grid[i][j] < min(grid[i][j-1], grid[i-1][j], grid[i+1][j]):
                    risk_value += grid[i][j] + 1

            elif grid[i][j] < min(grid[i-1][j], grid[i][j-1], grid[i][j+1], grid[i+1][j]):
                risk_value += grid[i][j] + 1

    print(risk_value)
