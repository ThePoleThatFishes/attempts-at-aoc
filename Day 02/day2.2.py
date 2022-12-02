with open("day2_input.txt", "r") as f:  
    matches = [line.strip() for line in f]
    points = matches.count("A X") * 3 + matches.count("A Y") * 4 + matches.count("A Z") * 8 +\
        matches.count("B X") * 1 + matches.count("B Y") * 5 + matches.count("B Z") * 9 +\
        matches.count("C X") * 2 + matches.count("C Y") * 6 + matches.count("C Z") * 7
    print(points)
