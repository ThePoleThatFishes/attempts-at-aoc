with open("day10_input.txt", "r") as f:
    x = 1
    add2x = 0
    screen = ""

    for cycle in range(1, 241):
        if (cycle - 1) % 40 <= x + 1 <= (cycle + 1) % 40:
            screen += "%"
        else:
            screen += "."

        print(cycle, x + 1, (cycle - 1) % 40, (cycle + 1) % 40)

        if not add2x:
            instruction = f.readline().strip()
        else:
            x += add2x
            add2x = 0
            continue

        if "addx" in instruction:
            add2x = int(instruction.split(" ")[1])
            continue

for i in range(6):
    print(screen[40*i: 40*(i+1)])
