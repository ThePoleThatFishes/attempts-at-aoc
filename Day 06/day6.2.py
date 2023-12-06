with open("day6_input.txt", "r") as f:
    wins = 0
    for line in f:
        if "Time:" in line:
            time = int(line.strip().split("Time:        ")[1].replace("     ", " ").replace(" ", ""))
        if "Distance:" in line:
            distance = int(line.strip().split("Distance:   ")[1].replace("   ", ""))

    for i in range(time):
        if i*(time-i) > distance:
            wins += 1
    print(wins)