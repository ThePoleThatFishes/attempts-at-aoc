with open("day2_input.txt", "r") as f:
    safe = 0
    sort_forward_list = []
    sort_reverse_list = []
    num_list = []
    for line in f.readlines():
        num_list = list(map(int, line.strip("\n").split(" ")))
        sort_forward_list = sorted(num_list)
        sort_reverse_list = sorted(num_list, reverse=True)

        def check_safety(num_list, sort_forward_list, sort_reverse_list):
            is_safe = True
            if num_list != sort_forward_list and num_list != sort_reverse_list:
                return False
            else:
                for i in range(len(num_list) - 1):
                    if not (1 <= abs(num_list[i] - num_list[i+1]) <= 3):
                        is_safe = False
                        break
                if is_safe:
                    return True

        if check_safety(num_list, sort_forward_list, sort_reverse_list):
            safe += 1
        else:
            for j in range(len(num_list)):
                num_temp_list = num_list[0:j] + num_list[j+1:]
                print(num_list, num_temp_list)
                if check_safety(num_temp_list, sorted(num_temp_list), sorted(num_temp_list, reverse=True)):
                    safe += 1
                    break
    print(safe)
