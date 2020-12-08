numlist = []


with open("day1_data.txt", "r") as f:
    for num in f:
        numlist.append(int(num))

    for i in range(len(numlist)):
        for j in range(len(numlist) - 1):
            if numlist[i] + numlist[j] == 2020:
                print(numlist[i] * numlist[j])
