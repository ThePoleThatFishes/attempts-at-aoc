with open("day4_input.txt", "r") as f:
    instances = 0
    for line in f:
        assignment = line.strip().split(",")
        elf_1 = assignment[0].split("-")
        elf_2 = assignment[1].split("-")
        if (int(elf_1[0]) >= int(elf_2[0]) and int(elf_1[1]) <= int(elf_2[1])) or\
                (int(elf_1[0]) <= int(elf_2[0]) and int(elf_1[1]) >= int(elf_2[1])):
            instances += 1
    print(instances)
