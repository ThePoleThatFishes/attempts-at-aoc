with open("day2_input.txt", "r") as f:
    counter = 0
    for line in f:
        game = line.strip("\n").split(": ")
        rounds = game[1].split("; ")
        min_cubes = [0, 0, 0]  # red, green, blue
        for rnd in rounds:
            cubes = [(int(cube.split(" ")[0]), cube.split(" ")[1]) for cube in rnd.split(", ")]
            for cube in cubes:
                if cube[1] == "red":
                    min_cubes[0] = max(min_cubes[0], cube[0])
                elif cube[1] == "green":
                    min_cubes[1] = max(min_cubes[1], cube[0])
                elif cube[1] == "blue":
                    min_cubes[2] = max(min_cubes[2], cube[0])
        counter += min_cubes[0] * min_cubes[1] * min_cubes[2]

    print(counter)