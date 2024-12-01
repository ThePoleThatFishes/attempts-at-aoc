with open("day1_input.txt", "r") as f:
    similarity = 0
    list1 = {}
    list2 = []
    for line in f.readlines():
        list2.append(int(line.strip("\n").split("   ")[1]))
        list1[int(line.strip("\n").split("   ")[0])] = 0
    for i in list(list1.keys()):
        list1[i] = list2.count(i)
        similarity += i * list1[i]
    print(similarity)