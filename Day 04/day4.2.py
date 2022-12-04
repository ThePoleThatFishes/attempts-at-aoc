with open("day4_input.txt", "r") as f:
    instances = 0
    for line in f:
        assignment = line.strip().split(",")
        elf_1_sections = set(range(int(assignment[0].split("-")[0]), int(assignment[0].split("-")[1]) + 1))
        elf_2_sections = set(range(int(assignment[1].split("-")[0]), int(assignment[1].split("-")[1]) + 1))

        if elf_1_sections & elf_2_sections:
            instances += 1
    print(instances)
