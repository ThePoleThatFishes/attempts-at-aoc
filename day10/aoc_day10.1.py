with open("day10_data.txt", "r") as f:
    adapters = [0]
    for line in f:
        adapters.append(int(line))
    adapters.sort()
    voltage = 0
    potential1, potential3 = 0, 0
    for i in range(1, len(adapters)):

        if adapters[i] - adapters[i-1] == 3:
            potential3 += 1
        elif adapters[i] - adapters[i-1] == 1:
            potential1 += 1
    answer = (potential3 + 1) * potential1
    print(answer)
