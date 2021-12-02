numlist = []
counter = 0

with open("day1_input.txt", "r") as f:
    for num in f:
        numlist.append(int(num))
        if len(numlist) > 3:
            if sum(numlist[-2:-5:-1]) < sum(numlist[-1:-4:-1]):
                counter += 1

    print(counter)
    f.close()

