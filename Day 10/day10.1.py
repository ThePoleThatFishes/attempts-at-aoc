with open("day10_input.txt", "r") as f:
    f2 = open("day10.2_input.txt", "w")
    navsys = [line.strip("\n") for line in f]
    pairs = ("<>", "()", "[]", "{}")
    error_score = 0
    safe_chunks = []
    for chunks in navsys:
        chunk_list = []
        flag = False
        for char in chunks:
            chunk_list.append(char)
            if len(chunk_list) == 1:
                continue
            if char in (">", ")", "]", "}"):
                if chunk_list[-2] + chunk_list[-1] not in pairs:
                    if char == ">":
                        error_score += 25137
                    elif char == "}":
                        error_score += 1197
                    elif char == "]":
                        error_score += 57
                    else:
                        error_score += 3
                    flag = True
                    break

                else:
                    chunk_list = chunk_list[:-2]

        if not flag:
            f2.write(chunks + "\n")

    print(error_score)

