with open("day2_input.txt", "r") as f:
    counter = 0
    for line in f:
        game = line.strip("\n").split(": ")
        game_id = int(game[0].split(" ")[1])
        rounds = game[1].replace(";", ",").split(", ")
        cubes = [(int(cube_obj.split(" ")[0]), cube_obj.split(" ")[1]) for cube_obj in rounds]
        count = True
        for cube_tuple in cubes:
            if cube_tuple[0] > 14:
                count = False
                break
            elif cube_tuple[0] > 13:
                if cube_tuple[1] != "blue":
                    count = False
                    break
            elif cube_tuple[0] > 12:
                if cube_tuple[1] == "red":
                    count = False
                    break
        if count:
            counter += game_id

print(counter)