with open("day8_data.txt", "r") as f:
    accval = 0
    runinst = []
    inst = []
    for line in f:
        inst.append(line.replace("\n", ""))
    currinst = 0
    while True:
        if runinst.count(currinst) > 1:
            print(runinst)
            print("Accumulated Value: {}".format(accval))
            break

        if inst[currinst][0:3] == "acc":
            accval += int(inst[currinst][4:])
            currinst += 1
        elif inst[currinst][0:3] == "jmp":
            currinst += int(inst[currinst][4:])
        elif inst[currinst][0:3] == "nop":
            currinst += 1
        runinst.append(currinst)
