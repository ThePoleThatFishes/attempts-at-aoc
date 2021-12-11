with open("day8_input.txt", "r") as f:
    segments = {2: 0, 3: 0, 4: 0, 7: 0}
    for line in f:
        line = line[line.index("|") + 2:].strip("\n").split(" ")
        for wiring in line:
            if len(wiring) in list(segments.keys()):
                segments[len(wiring)] += 1

    print(sum(segments.values()))
    f.close()
