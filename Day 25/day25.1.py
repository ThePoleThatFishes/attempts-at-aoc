with open("day25_input.txt", "r") as f:
    snafu2int = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    int2snafu = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    number = 0
    number5 = []
    output = ""
    for line in f:
        snafu = line.strip()
        for i in range(len(snafu)):
            number += snafu2int[snafu[i]] * (5 ** (len(snafu) - 1 - i))

    def int2five(num):
        number5.append(num % 5)
        num = num // 5
        if num:
            int2five(num)
        else:
            number5.append(0)

    int2five(number)

    for i in range(len(number5)):
        if number5[i] > 2:
            number5[i] -= 5
            number5[i+1] += 1

    for i in range(-2, -len(number5) - 1, -1):
        number5[i] = int2snafu[number5[i]]
        output += number5[i]

    print(output)
