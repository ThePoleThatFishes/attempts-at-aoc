import re


with open("day5.1_data.txt", "r") as f:
    seatIDs = []
    maxID = 0
    for bp in f:
        bp = re.sub("[FL]", "0", bp)
        bp = re.sub("[BR]", "1", bp)
        row = 0
        col = 0
        for i in range(7):
            row += int(bp[i])*pow(2, 6-i)
        for i in range(7, 10):
            col += int(bp[i])*pow(2, 9-i)
        seatID = row*8 + col
        seatIDs.append(seatID)
        maxID = max(maxID, seatID)
    print(maxID)

    for i in range(maxID + 1):
        if i not in seatIDs:
            print("Missing seat: {}".format(i))



