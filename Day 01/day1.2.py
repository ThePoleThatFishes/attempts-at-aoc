import re

with open("day1_input.txt", "r") as f:
    result = 0
    for line in f:
        line.strip("\n")
        num2int = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                   "eight": "8", "nine": "9"}
        print(line)
        for k, v in num2int.items():
            line = line.replace(k, v)
        print(line)
        nums = re.findall("[0-9]+", line)
        numstring = ""
        for item in nums:
            numstring += item
        print(numstring)
        result += int(numstring[0] + numstring[-1])
    print(result)
