with open("day5.1_data.txt", "r") as f:
    seatIDs = []
    maxID = 855
    for bp in f:
        minrow = 0
        maxrow = 127
        mincol = 0
        maxcol = 7
        for char in bp:
            distrow = maxrow - minrow + 1
            distcol = maxcol - mincol + 1
            if char == "F":
                maxrow -= distrow//2
            elif char == "B":
                minrow += distrow//2
            elif char == "L":
                mincol += distcol//2
            elif char == "R":
                maxcol -= distcol//2

        seatID = minrow*8 + mincol
        seatIDs.append(seatID)
    seatIDs.sort()
for i in range(maxID + 1):
    if (i - 1 in seatIDs) and (i + 1 in seatIDs):
        if i not in seatIDs:
            print(i)
