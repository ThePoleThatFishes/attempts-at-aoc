from string import ascii_lowercase

with open("day6_data.txt", "r") as f:
    yes = 0
    members = 0
    group = ""
    letters = ascii_lowercase
    for answers in f:
        if answers != "\n":
            members += 1
            group += answers
        elif answers == "\n":
            for char in letters:
                if group.count(char) == members:
                    yes += 1
            group = ""
            members = 0
    for char in letters:
        if group.count(char) == members:
            yes += 1

print(yes)
