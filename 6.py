with open('6.txt', 'r') as f:
    lines = f.readlines()

for stream in lines:
    mark = []
    [mark.append('') for _ in range(14)]  # change for amount
    count = 0
    printed = False
    for i in stream:
        mark.pop(0)
        mark.append(i)
        count += 1
        if '' not in mark:
            dup = False
            for j in mark:
                _ = mark.copy()
                _.remove(j)
                if j in _:
                    dup = True
                    break
            if not dup and not printed:
                print(count)
                printed = True
