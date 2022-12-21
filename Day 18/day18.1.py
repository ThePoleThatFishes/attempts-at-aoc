with open("day18_input.txt", "r") as f:
    x, y, z = [], [], []
    surface = 0

    def count_neighbors(x, y, z):
        neighbors = 0
        if cube[x-1][y][z]:
            neighbors += 1
        if cube[x+1][y][z]:
            neighbors += 1
        if cube[x][y-1][z]:
            neighbors += 1
        if cube[x][y+1][z]:
            neighbors += 1
        if cube[x][y][z-1]:
            neighbors += 1
        if cube[x][y][z+1]:
            neighbors += 1
        return neighbors
    for line in f:
        coords = line.strip().split(",")
        x.append(int(coords[0]))
        y.append(int(coords[1]))
        z.append(int(coords[2]))
    cube = [[[False for i in range(max(z) + 3)] for j in range(max(y) + 3)] for k in range(max(x) + 3)]
    for i in range(len(x)):
        cube[x[i] + 1][y[i] + 1][z[i] + 1] = True
    print(min(x), min(y), min(z))
    for i in range(1, max(x) + 2):
        for j in range(1, max(y) + 2):
            for k in range(1, max(z) + 2):
                if cube[i][j][k]:
                    surface += (6 - count_neighbors(i, j, k))

print(surface)
