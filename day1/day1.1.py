numlist = []
count = 0

with open("day1_input.txt", "r") as f:
    for num in f:
        numlist.append(int(num))
        if len(numlist) > 1:
            if numlist[-1] > numlist[-2]:
                count += 1
      
    print(count)
    f.close()