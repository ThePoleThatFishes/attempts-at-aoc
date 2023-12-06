with open("day6_input.txt", "r") as f:
    margin = 1
    for line in f:
        if "Time:" in line:
            times = list(map(int, line.strip().split("Time:        ")[1].replace("     ", " ").split(" ")))
        if "Distance:" in line:
            distances = list(map(int, line.strip().split("Distance:   ")[1].split("  ")))

    for i in range(len(distances)):
        wins = 0
        for j in range(times[i]):
            distance = j*(times[i]-j)
            if distance > distances[i]:
                wins += 1
        margin *= wins

    print(margin)