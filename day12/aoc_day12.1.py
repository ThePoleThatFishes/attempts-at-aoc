from math import sin, cos, pi
boat = [0, 0, 0]

with open("day12_data.txt", "r") as f:
    for line in f:
        if "L" in line:
            boat[2] += int(line[1:])*pi/180
        elif "R" in line:
            boat[2] -= int(line[1:])*pi/180
        elif "N" in line:
            boat[1] += int(line[1:])
        elif "S" in line:
            boat[1] -= int(line[1:])
        elif "E" in line:
            boat[0] += int(line[1:])
        elif "W" in line:
            boat[0] -= int(line[1:])
        else:
            boat[0] += int(line[1:])*cos(boat[2])
            boat[1] += int(line[1:])*sin(boat[2])
    print(abs(boat[0]) + abs(boat[1]))
