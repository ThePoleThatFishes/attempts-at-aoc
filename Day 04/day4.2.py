with open("day4_input.txt", "r") as f:
    cards = {i: 1 for i in range(1, 193)}
    for line in f:
        card_id = int(line.strip().split(": ")[0].split(" ")[-1])
        numbers = line.strip().split(": ")[1].replace("  ", " ").strip()
        winning = numbers.split(" | ")[0].split(" ")
        own_numbers = numbers.split(" | ")[1].split(" ")
        winners = 0
        for num in own_numbers:
            if num in winning:
                winners += 1
                try:
                    cards[card_id+winners] += cards[card_id]
                except KeyError:
                    break
    print(sum(cards.values()))