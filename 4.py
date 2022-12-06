with open('4.txt', 'r') as f:
    id_sections = f.readlines()
total = 0
for i in id_sections:
    x, y = i.split(',')
    x = x.split('-')
    y = y.split('-')
    if int(x[1]) - int(x[0]) > int(y[1]) - int(y[0]):
        _ = x
        x = y
        y = _
    if int(int(x[0]) >= int(y[0]) and int(x[1]) <= int(y[1])):
        total += 1
print(total)

# PART 2

total = 0
for i in id_sections:
    x, y = i.split(',')
    x = x.split('-')
    y = y.split('-')
    if int(x[1]) - int(x[0]) > int(y[1]) - int(y[0]):
        _ = x
        x = y
        y = _
    if int(int(x[0]) <= int(y[1]) and int(x[1]) >= int(y[0])):
        total += 1
print(total)
