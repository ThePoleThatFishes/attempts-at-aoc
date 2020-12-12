from math import sin, cos, pi
boat = [0, 0]
wp = [10, 1]

with open("day12_data.txt", "r") as f:
    for line in f:
        if "L" in line:
            rads = int(line[1:])*pi/180
            wp = [round(wp[0]*cos(rads) - wp[1]*sin(rads), 1), round(wp[0]*sin(rads) + wp[1]*cos(rads), 1)]
        elif "R" in line:
            rads = -int(line[1:]) * pi / 180
            wp = [round(wp[0]*cos(rads) - wp[1]*sin(rads), 1), round(wp[0]*sin(rads) + wp[1]*cos(rads), 1)]
        elif "N" in line:
            wp[1] += int(line[1:])
        elif "S" in line:
            wp[1] -= int(line[1:])
        elif "E" in line:
            wp[0] += int(line[1:])
        elif "W" in line:
            wp[0] -= int(line[1:])
        else:
            boat[0] += int(line[1:])*wp[0]
            boat[1] += int(line[1:])*wp[1]
    print(int(abs(boat[0]) + abs(boat[1])))
