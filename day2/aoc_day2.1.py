with open("day2_data.txt", "r") as f:
    validpwds = 0
    for pwd in f:
        dash = pwd.find("-")
        colon = pwd.find(":")
        space = pwd.find(" ")
        minchars = int(pwd[:dash])
        maxchars = int(pwd[dash + 1:space + 1])
        char = pwd[colon - 1]
        word = pwd[colon + 2:]
        if minchars <= word.count(char) <= maxchars:
            validpwds += 1
    print(validpwds)
