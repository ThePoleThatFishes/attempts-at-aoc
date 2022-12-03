import string

with open("day3_input.txt", "r") as f:
    priority = string.ascii_letters
    total_priority = 0
    for line in f:
        backpack1 = line.strip()[:(len(line.strip()) + 1) // 2]
        backpack2 = line.strip()[(len(line.strip())) // 2:]
        for char in backpack1:
            if char in backpack2:
                common_item = char
                break
        total_priority += priority.index(common_item) + 1

    print(total_priority)
