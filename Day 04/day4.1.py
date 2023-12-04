with open("day4_input.txt", "r") as f:
    points = 0
    for line in f:
        numbers = line.strip().split(": ")[1].replace("  ", " ").strip()
        winning = numbers.split(" | ")[0].split(" ")
        own_numbers = numbers.split(" | ")[1].split(" ")
        winners = 0
        for num in own_numbers:
            if num in winning:
                winners += 1
        if winners:
            points += 2 ** (winners - 1)
        print(winners)

    print(points)
