class Monkey:
    def __init__(self, num, inv: list, op, div, iftrue, iffalse, inspects):
        self.id = num
        self.inventory = inv
        self.operation = op
        self.divisibility = div
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.inspects = inspects


monkeys = [Monkey(0, [54, 98, 50, 94, 69, 62, 53, 85], "* 13", "% 3", 2, 1, 0),
           Monkey(1, [71, 55, 82], "+ 2", "% 13", 7, 2, 0),
           Monkey(2, [77, 73, 86, 72, 87], "+ 8", "% 19", 4, 7, 0),
           Monkey(3, [97, 91], "+ 1", "% 17", 6, 5, 0),
           Monkey(4, [78, 97, 51, 85, 66, 63, 62], "* 17", "% 5", 6, 3, 0),
           Monkey(5, [88], "+ 3", "% 7", 1, 0, 0),
           Monkey(6, [87, 57, 63, 86, 87, 53], "** 2", "% 11", 5, 0, 0),
           Monkey(7, [73, 59, 82, 65], "+ 6", "% 2", 4, 3, 0)]

for j in range(20):
    for monkey in monkeys:
        for i in range(len(monkey.inventory)):
            monkey.inventory[i] = eval(f"monkey.inventory[i] {monkey.operation}")
            monkey.inventory[i] = monkey.inventory[i] // 3
            monkey.inspects += 1
            if not eval(f"monkey.inventory[i] {monkey.divisibility}"):
                monkeys[monkey.iftrue].inventory.append(monkey.inventory[i])
            else:
                monkeys[monkey.iffalse].inventory.append(monkey.inventory[i])
        monkey.inventory.clear()

shenanigans = sorted([monkey.inspects for monkey in monkeys])
print(shenanigans[-2] * shenanigans[-1])

