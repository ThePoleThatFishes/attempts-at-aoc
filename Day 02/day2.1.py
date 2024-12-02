with open("day2_input.txt", "r") as f:
    safe = 0
    sort_forward_list = []
    sort_reverse_list = []
    num_list = []
    for line in f.readlines():
        num_list = list(map(int, line.strip("\n").split(" ")))
        sort_forward_list = sorted(num_list)
        sort_reverse_list = sorted(num_list, reverse=True)
        is_safe = True
        if num_list != sort_forward_list and num_list != sort_reverse_list:
            continue
        else:
            for i in range(len(num_list) - 1):
                if not (1 <= abs(num_list[i] - num_list[i+1]) <= 3):
                    is_safe = False
                    break
            if is_safe:
                safe += 1
    print(safe)
