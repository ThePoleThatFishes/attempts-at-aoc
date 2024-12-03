import re

with open("day3_input.txt", "r") as f:
    result = 0
    file_contents = f.read()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", file_contents)
    for item in matches:
        matches = list(map(int, re.findall(r'\d{1,3}', item)))
        result += matches[0] * matches[1]
    print(result)
