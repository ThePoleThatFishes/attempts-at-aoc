from string import ascii_lowercase

with open("day6_data.txt", "r") as f:
    yes = 0
    group = ""
    letters = ascii_lowercase
    for answers in f:
        if answers != "\n":
            group += answers
        elif answers == "\n":
            for char in letters:
                if char in group:
                    yes += 1
            group = ""
    for char in letters:
        if char in group:
            yes += 1

print(yes)
