with open('5.txt', 'r') as f:
    var = f.readlines()

for i in range(len(var)):
    # print(len(var[i]))
    if len(var[i]) == 1:
        contents_lines = var[:i-1]
        instruction_lines = var[i+1:]
        break
content = []
[content.append([]) for x in range((len(contents_lines[0])+1)//4)]
# print(contents_lines)
for i in contents_lines:
    count = 0
    for j in range(1, len(i), 4):
        # print(count)
        if i[j] != " ":
            content[count].append(i[j])
        count += 1
[content[_].reverse() for _ in range(len(content))]
# print(content)
instruct = []
[instruct.append(x.split(' ')) for x in instruction_lines]

for i in instruct:
    vals = content[int(i[3])-1][-int(i[1]):]
    # vals.reverse() #only inculde for part 1
    content[int(i[3])-1] = content[int(i[3])-1][:-int(i[1])]
    content[int(i[5])-1].extend(vals)
    # print(content)

print(content)
out = []
[out.append(i[-1]) for i in content]
out = ''.join(out)
print(out)
