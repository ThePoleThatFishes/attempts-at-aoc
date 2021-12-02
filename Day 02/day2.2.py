horizontal_pos = 0
vertical_pos = 0
aim = 0

with open("day2_input.txt", "r") as f:
    for line in f:
        directions = line.split()
        if directions[0] == "down":
            aim += int(directions[1])
        elif directions[0] == "up":
            aim -= int(directions[1])
        else:
            horizontal_pos += int(directions[1])
            vertical_pos += aim * int(directions[1])

print(vertical_pos * horizontal_pos)
