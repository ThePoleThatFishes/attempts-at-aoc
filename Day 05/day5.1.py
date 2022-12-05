import re

with open("day5_input.txt", "r") as f:
    crates = {1: "rgjbtvz", 2: "jrvl", 3: "sqf", 4: "zhnlfvqg", 5: "rqtjcsmw", 6: "swtchf",
              7: "dzcvfnj", 8: "lgzdwrfq", 9: "jbwvp"}
    lines = f.readlines()
    for i in range(10, len(lines)):
        move_crates = re.findall("[0-9]+", lines[i])
        for j in range(int(move_crates[0])):
            crates[int(move_crates[2])] += crates[int(move_crates[1])][-1 -j]
        crates[int(move_crates[1])] = crates[int(move_crates[1])][:-int(move_crates[0])]

    for value in crates.values():
        print(value[-1])