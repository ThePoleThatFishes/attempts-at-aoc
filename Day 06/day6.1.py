with open("day6_input.txt", "r") as f:
    chars = f.read().strip()
    for i in range(len(chars)):
        group = set(chars[i:i+4])
        if len(group) == 4:
            print(i+4)
            break
