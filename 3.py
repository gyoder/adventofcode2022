with open('3.txt', 'r') as f:
    runsacks = f.readlines()

priority = {}

for i in range(1,27):
    priority[chr(96+i)] = i
for i in range(27,53):
    priority[chr(64+i-26)] = i

count = {}

'''
this isnt the challenge, i cant read
for i in runsacks:
    for j in i[:-1]:
        for k in j:
            for l in runsacks:
            
                if l == i[:-1]: pass
                if k in l:
                    if k in count:
                        count[k] += 1
                    else:
                        count[k] = 1
'''

for i in runsacks:
    for j in i[:len(i)//2]:
        if j in i[len(i)//2:]:
            if j in count:
                count[j] += 1
            else: 
                count[j] = 1
            break
#print(count)
score = 0
#print(priority)
for i in count.keys():
    score += (priority[i]*count[i])
print(score)

#PART 2
all_badge = []
for i in range(0,len(runsacks),3):
    #allcontain = runsacks[i].split('')
    ballcontain = [*runsacks[i]]
    allcontain = []
    [allcontain.append(x) for x in ballcontain if x not in allcontain]
    allcontain.remove('\n')
    while len(allcontain) != 1:
        for j in runsacks[i:i+3]:
            for k in allcontain:
                if k not in j:
                    allcontain.remove(k)
    all_badge.append(allcontain[0])

total = 0
for i in all_badge:
    total += priority[i]
print(total)


