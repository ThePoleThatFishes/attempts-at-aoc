with open("day5_input.txt", "r") as f:
    min_location = 2 ** 50 - 1
    data = [[] for i in range(7)]
    map_found = False
    counter = -1
    for line in f:
        line = line.strip()

        if line.startswith("seeds: "):
            seeds = list(map(int, line.split(" ")[1:]))

        if "map" in line:
            map_found = True
            continue

        if line == "":
            map_found = False
            counter += 1

        if map_found:
            transfer_map = list(map(int, line.split(" ")))
            data[counter] += [transfer_map]

    for seed in seeds:
        location = seed
        print(seed)
        for i in range(len(data)):
            print(data[i])
            for j in range(len(data[i])):
                print(data[i][j], data[i][j][1] + data[i][j][2] - 1, location)
                if data[i][j][1] <= location <= data[i][j][1] + data[i][j][2] - 1:
                    location += data[i][j][0] - data[i][j][1]
                    break
        min_location = min(min_location, location)

    print(min_location)