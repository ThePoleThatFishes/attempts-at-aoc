with open("day14_input.txt", "r") as f:
        
    polymer = f.readline().strip("\n")
    rules = {}
    for line in f:
        if line.startswith("\n"):
            pass
        else:
            find_pair = line[:line.index(" ")]
            rules[find_pair] = line[line.index(">") + 2]
    
    for i in range(10):       
        insertions = {}
        
        for i in range(len(polymer) - 1):
            pair = polymer[i] + polymer[i+1]
            if pair in list(rules.keys()):
               insertions[i + 1 + len(insertions.keys())] = rules[pair]
                                   
        
        for pos, element in insertions.items():
            polymer = f"{polymer[:pos]}{element}{polymer[pos:]}"

    
    charcounter = {}    
    for char in polymer:
        try:
            charcounter[char] += 1
        except KeyError:
            charcounter[char] = 1
    values = list(charcounter.values())
    print(max(values) - min(values))
        
