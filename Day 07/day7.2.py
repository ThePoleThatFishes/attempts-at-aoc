with open("day7_input.txt", "r") as f:
    hands = {"high card": [], "1 pair": [], "2 pairs": [], "3 of a kind": [], "full house": [], "4 of a kind": [],
             "5 of a kind": []}
    hands2wagers = {}
    score = 0
    i = 0
    for line in f:
        hand = line.strip().split(" ")[0].replace("A", "D").replace("K", "C").replace("Q", "B")\
            .replace("J", "1").replace("T", "A")
        wager = int(line.strip().split(" ")[1])
        hands2wagers[hand] = wager

        cards = "123456789ABCD"
        contents = []
        for card in cards:
            contents.append(hand.count(card))

        if 5 in contents or max(contents[1:]) + contents[0] == 5:
            hands["5 of a kind"].append(hand)
        elif 4 in contents or max(contents[1:]) + contents[0] == 4:
            hands["4 of a kind"].append(hand)
        elif 3 in contents or max(contents[1:]) + contents[0] == 3:
            if (2 in contents and 3 in contents) or (contents.count(2) == 2 and contents[0] == 1):
                hands["full house"].append(hand)
            else:
                hands["3 of a kind"].append(hand)
        elif 2 in contents or max(contents[1:]) + contents[0] == 2:
            if contents.count(2) == 2 or (contents[0] == 1 and contents.count(2) == 1):
                hands["2 pairs"].append(hand)
            else:
                hands["1 pair"].append(hand)
        else:
            hands["high card"].append(hand)

    for key in hands.keys():
        hands[key].sort()
        for hand in hands[key]:
            score += (i+1)*hands2wagers[hand]
            i += 1

    print(score)
