with open("day1_input.txt", "r") as f:
    elven_inventories = []
    calories = 0
    for line in f:
        if line.strip() == "":
            elven_inventories.append(calories)
            calories = 0
        else:
            calories += int(line.strip())
    print(max(elven_inventories))
