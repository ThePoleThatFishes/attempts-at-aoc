import string

with open("day3_input.txt", "r") as f:
    priority = string.ascii_letters
    total_priority = 0
    backpacks = list(f)
    for i in range(0, len(backpacks), 3):
        for char in backpacks[i]:
            if char in backpacks[i+1] and char in backpacks[i+2]:
                common_item = char
                break
        total_priority += priority.index(common_item) + 1

    print(total_priority)
