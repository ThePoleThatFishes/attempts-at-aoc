with open("day5.1_data.txt", "r") as f:
    maxID = 0
    seatID = 0
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
            elif char == "R":
                mincol += distcol//2
            elif char == "L":
                maxcol -= distcol//2

        seatID = minrow*8 + mincol
        maxID = max(seatID, maxID)
    print(maxID)
