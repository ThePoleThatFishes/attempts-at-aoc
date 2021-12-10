with open("day10.2_input.txt", "r") as f:
    navsys = [line.strip("\n") for line in f]
    pairs = ("<>", "()", "[]", "{}")
    correction_score = []
    safe_chunks = []
    for chunks in navsys:
        chunk_list = []
        for char in chunks:
            chunk_list.append(char)
            if len(chunk_list) == 1:
                continue
            if char in (">", ")", "]", "}"):
                chunk_list = chunk_list[:-2]

        missing_brackets = ""
        for char in reversed(chunk_list):
            for pair in pairs:
                if char == pair[0]:
                    missing_brackets += pair[1]
                    break

        chunk_correction_score = 0
        for char in missing_brackets:
            chunk_correction_score *= 5
            chunk_correction_score += (")", "]", "}", ">").index(char) + 1

        correction_score.append(chunk_correction_score)

    correction_score.sort()
    print((correction_score[int((len(correction_score) - 1)/2)]))
