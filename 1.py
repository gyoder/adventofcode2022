with open("1.txt", "r") as f:
    callist = ''.join(f.readlines())
calories = []
for i in callist.split("\n\n"):
    total = 0
    for j in i.split('\n'):
        # print(i.split('\n'))
        total += int(j)
    calories.append(total)

calories.sort()
print(f'The elf with the most calories has {calories[-1]} calories')
print(f'The top 3 elves have {sum(calories[-3:])} in total')
