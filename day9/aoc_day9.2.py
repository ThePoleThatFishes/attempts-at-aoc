with open("day9_data.txt", "r") as f:
    preamble = []
    for line in f:
        preamble.append(int(line))
    invalidnum = 530627549
    succesivenums = []
    for i in range(len(preamble)):
        for j in range(i, len(preamble)):
            succesivenums.append(preamble[j])
            if sum(succesivenums) == invalidnum and len(succesivenums) >= 2:
                print(min(succesivenums) + max(succesivenums))
                break
            elif sum(succesivenums) > invalidnum:
                succesivenums = []
                break
