with open("day7_input.txt", "r") as f:
    hands = {"high card": [], "1 pair": [], "2 pairs": [], "3 of a kind": [], "full house": [], "4 of a kind": [],
             "5 of a kind": []}
    cards = "23456789ABCDE"
    hands2wagers = {}
    score = 0
    i = 0
    for line in f:
        hand = line.strip().split(" ")[0].replace("A", "E").replace("K", "D").replace("Q", "C")\
            .replace("J", "B").replace("T", "A")
        wager = int(line.strip().split(" ")[1])
        hands2wagers[hand] = wager
        stop = False

        for char in cards:
            if hand.count(char) == 5:
                hands["5 of a kind"].append(hand)
                break
            elif hand.count(char) == 4:
                hands["4 of a kind"].append(hand)
                break
            elif hand.count(char) == 3:
                for char2 in cards[:cards.index(char)] + cards[cards.index(char)+1:]:
                    if hand.count(char2) == 2:
                        hands["full house"].append(hand)
                        stop = True
                        break
                else:
                    hands["3 of a kind"].append(hand)
                    break
            elif hand.count(char) == 2:
                for char2 in cards[:cards.index(char)] + cards[cards.index(char)+1:]:
                    if hand.count(char2) == 3:
                        hands["full house"].append(hand)
                        stop = True
                        break
                    if hand.count(char2) == 2:
                        hands["2 pairs"].append(hand)
                        stop = True
                        break

                else:
                    hands["1 pair"].append(hand)
                    break
            if stop:
                break
        else:
            hands["high card"].append(hand)

    for key in hands.keys():
        hands[key].sort()
        for hand in hands[key]:
            score += (i+1)*hands2wagers[hand]
            i += 1

    print(score)