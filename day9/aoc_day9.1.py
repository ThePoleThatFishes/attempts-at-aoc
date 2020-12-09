with open("day9_data.txt", "r") as f:
    preamble = []
    for line in f:
        preamble.append(int(line))
    for i in range(975):
        currpreamble = preamble[i:i+25]
        found = True
        for j in range(len(currpreamble)):
            for k in range(len(currpreamble) - 1):
                if preamble[i+25] == currpreamble[j] + currpreamble[k]:
                    found = False
        if found:
            print("Invalid Number: {:,}\nPreamble Start: {}".format(preamble[i+25], i))
            break

