numlist = []


with open("day1_data.txt", "r") as f:
    for num in f:
        numlist.append(int(num))

    for i in range(len(numlist)):
        for j in range(len(numlist) - 1):
            for k in range(len(numlist) - 2):
                if numlist[i] + numlist[j] + numlist[k] == 2020:
                    print(numlist[i] * numlist[j] * numlist[k])
