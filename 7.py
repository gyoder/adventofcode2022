import dpath
import json


def mkdir(list, path, name):
    pass


def total_folder(dir):
    global full_total, dir_sizes
    total = 0
    for i in dir.values():
        if type(i) == type(1):  # bad
            total += i
        else:
            _ = total_folder(i)
            dir_sizes.append(_)
            total += _
            if _ < 100000:
                full_total += _
    return total


with open('7.txt', 'r') as f:
    commands = f.read().splitlines()

# I cannot be assed to do this the correct way so imma do it dumb
dir_sizes = []
full_total = 0
files = {}
pwd = []
mode = 'command'
for command in commands:
    c = command.split(' ')
    # print(c)
    if c[0] == '$':
        if c[1] == 'cd':
            if c[2] == '..':
                pwd.pop(len(pwd)-1)
            else:
                pwd.append(c[2])
        elif c[1] == 'ls':
            tmp_pwd = pwd.copy()
            # print('a')
            if len(c) == 3:
                tmp_pwd.append(c[2])
    else:
        try:
            dpath.new(files, '/'.join(tmp_pwd)+'/'+c[1], int(c[0]))
        except:
            pass
            #dpath.new(files, '/'.join(tmp_pwd)+'/'+c[1], int(c[0]))


#print(json.dumps(files, indent=4))
used = total_folder(files)
unused = 70000000 - used
dir_sizes.sort()
# dir_sizes.reverse()
for i in dir_sizes:
    if i + unused > 30000000:
        print(i)
        break
# print(full_total)
