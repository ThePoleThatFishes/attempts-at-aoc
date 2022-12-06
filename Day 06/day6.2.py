with open("day6_input.txt", "r") as f:
    chars = f.read().strip()
    for i in range(len(chars)):
        group = set(chars[i:i+14])
        if len(group) == 14:
            print(i+14)
            break
