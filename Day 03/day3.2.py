import re

with open("day3_input.txt", "r") as f:
    result = 0
    file_contents = f.read()
    enabled = True
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", file_contents)
    print(matches)
    for item in matches:
        if item == "do()":
            enabled = True
            continue
        elif item == "don't()":
            enabled = False
            continue
        if enabled:
            matches = list(map(int, re.findall(r'\d{1,3}', item)))
            result += matches[0] * matches[1]

    print(result)
