with open("day2_data.txt", "r") as f:
    validpwds = 0
    for pwd in f:
        dash = pwd.find("-")
        colon = pwd.find(":")
        space = pwd.find(" ")
        pos1 = int(pwd[:dash]) - 1
        pos2 = int(pwd[dash + 1:space + 1]) - 1
        char = pwd[colon - 1]
        word = pwd[colon + 2:]
        print(pwd)
        print(pos1, pos2, char, word)
        if word[pos1] == char and word[pos2] == char:
            pass
        elif word[pos1] == char or word[pos2] == char:
            validpwds += 1
    print(validpwds)
