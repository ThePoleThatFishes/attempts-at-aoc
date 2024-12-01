with open("day1_input.txt", "r") as f:
    list1 = []
    list2 = []
    for line in f.readlines():
        list1.append(int(line.strip("\n").split("   ")[0]))
        list2.append(int(line.strip("\n").split("   ")[1]))
    list1 = sorted(list1)
    list2 = sorted(list2)
    list_distances = [abs(list2[i] - list1[i]) for i in range(len(list1))]
    print(sum(list_distances))
