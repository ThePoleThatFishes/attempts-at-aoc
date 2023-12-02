import re

with open("day1_input.txt", "r") as f:
    result = 0
    for line in f:
        line.strip("\n")
        nums = re.findall("[0-9]+", line)
        numstring = ""
        for item in nums:
            numstring += item
        result += int(numstring[0] + numstring[-1])
    print(result)
