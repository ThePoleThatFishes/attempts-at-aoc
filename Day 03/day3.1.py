with open("day3_input.txt", "r") as f:
    count = [0 for i in range(12)]  # keeps track of 1s - 0s at each position
    for line in f:
        for i in range(len(line) - 1):  # iterates through each number in the string
            if line[i] == "1":
                count[i] += 1
            else:
                count[i] -= 1

    gamma_int = 0
    for j in range(len(count)):  # conversion from "bin" to dec
        if count[j] > 0:  # if there's more 1s, add 2^(11-digit) to gamma
            gamma_int += 2 ** (11-j)
    epsilon_int = 2 ** 12 - 1 - gamma_int  # epsilon is basically the complementary to gamma, so 2^digits - 1 - gamma

    print(gamma_int * epsilon_int)
    f.close()
