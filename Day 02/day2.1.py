horizontal_pos = 0
vertical_pos = 0

with open("day2_input.txt", "r") as f:
    for line in f:
        directions = line.split()
        if directions[0] == "down":
            vertical_pos += int(directions[1])
        elif directions[0] == "up":
            vertical_pos -= int(directions[1])
        else:
            horizontal_pos += int(directions[1])

print(vertical_pos * horizontal_pos)
