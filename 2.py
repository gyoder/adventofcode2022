
with open('2.txt', 'r') as f:
    guide = f.readlines()

scores = {'X': 1, 'Y': 2, 'Z': 3}

map = {'X': 'A', 'Y': 'B', 'Z': 'C'}

order = map.values()
total = 0
for i in guide:
    c, r = i.split(' ')
    r = r[0]  # stupid newline things
    if c == map[r]:
        total += 3
    # this isnt great. i could probably make it much more readable
    elif r == list(map.keys())[(list(order).index(c)+1) % 3]:
        total += 6
    total += scores[r]

print(total)


# PART 2
real_total = 0
wdl = {'X': -1, 'Y': 0, 'Z': 1}
for i in guide:
    c, o = i.split(' ')
    o = o[0]  # stupid newline things
    r = list(map.keys())[(list(order).index(c)+wdl[o]) % 3]
    #print(list(order).index(c), wdl[o], r)
    if o == 'Y':
        real_total += 3
    if o == 'Z':
        real_total += 6
    real_total += scores[r]

print(real_total)
