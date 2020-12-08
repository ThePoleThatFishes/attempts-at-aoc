passport = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False,
            "cid": False}
valid = 0
validity = True

with open("day4.1.1_data.txt", "r") as f:
    for line in f:
        print(line, end="")
        for attr in passport.keys():
            if attr in line:
                passport[attr] = True
        if line == "\n":
            for attr in passport.keys():
                if not(passport[attr]) and attr != "cid":
                    validity = False
            print("{}, {}".format(passport, validity))
            if validity:
                valid += 1
            validity = True
            for attr in passport.keys():
                passport[attr] = False

print("\nValid passports: {}".format(valid))
