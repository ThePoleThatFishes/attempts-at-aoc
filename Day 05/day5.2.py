from math import atan, pi

with open("day5_input.txt", "r") as f:
    vents = []
    dict_coords = {}
    for line in f:
        line.strip("\n")
        pos1 = line[:line.index(" ") + 1]
        pos2 = line[line.index(" ") + 4:]
        pos1 = (int(pos1[:pos1.index(",")]), int(pos1[pos1.index(",") + 1:-1]))
        pos2 = (int(pos2[:pos2.index(",")]), int(pos2[pos2.index(",") + 1:]))
        vents.append([pos1, pos2])

    for coords in vents:

        try:
            slope = (coords[1][1] - coords[0][1]) / (coords[1][0] - coords[0][0])
        except ZeroDivisionError:
            pass

        if coords[0][0] == coords[1][0]:
            for i in range(min(coords[0][1], coords[1][1]), max(coords[0][1], coords[1][1]) + 1):
                try:
                    dict_coords[(coords[0][0], i)] += 1
                except KeyError:
                    dict_coords[(coords[0][0], i)] = 1

        elif coords[0][1] == coords[1][1]:
            for i in range(min(coords[0][0], coords[1][0]), max(coords[0][0], coords[1][0]) + 1):
                try:
                    dict_coords[(i, coords[0][1])] += 1
                except KeyError:
                    dict_coords[(i, coords[0][1])] = 1

        elif atan(abs(slope)) == pi / 4:
            for i in range(min(coords[0][0], coords[1][0]), max(coords[0][0], coords[1][0]) + 1):
                try:
                    dict_coords[(i, int(slope * i) - int(slope * coords[0][0]) + coords[0][1])] += 1
                except KeyError:
                    dict_coords[(i, int(slope * i) - int(slope * coords[0][0]) + coords[0][1])] = 1

    answer = 0
    for val in list(dict_coords.values()):
        if val >= 2:
            answer += 1

    print(answer)

    f.close()
