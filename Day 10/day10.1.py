with open("day10_input.txt", "r") as f:
    x = 1
    result = 0
    add2x = 0

    def cycle_check(result, cycle, x):
        if cycle in (20, 60, 100, 140, 180, 220):
            result += x * cycle
        return result

    for cycle in range(1, 221):
        result = cycle_check(result, cycle, x)

        if not add2x:
            instruction = f.readline().strip()
        else:
            x += add2x
            add2x = 0
            continue

        if "addx" in instruction:
            add2x = int(instruction.split(" ")[1])
            continue

    print(result)