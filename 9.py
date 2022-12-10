class cord:
    def __init__(self, c):
        self.c = c
    
    def __add__(self, other):
        return cord((self.c[0] + other.c[0], self.c[1] + other.c[1]))

    def __sub__(self, other):
        return cord((self.c[0] - other.c[0], self.c[1] - other.c[1]))
    
    def __str__(self):
        return str(self.c)

    def __eq__(self, other):
        return self.c[0] == other.c[0] and self.c[1] == other.c[1]
    
    def in_square(self, other):
        return (abs(self.c[0]-other.c[0]) <= 1) and (abs(self.c[1]-other.c[1]) <= 1)

    def move(self, other):
        x = (other.c[0]-self.c[0])
        if x != 0:
            x //= abs(x)
        y = other.c[1]-self.c[1]
        if y != 0:
            y //= abs(y)
        return cord((x,y))
        #return cord((other.c[0]-self.c[0])/abs(other.c[0]-self.c[0]), (other.c[1]-self.c[1])/abs(other.c[1]-self.c[1]))
    
    def __hash__(self) -> int:
        return (self.c[0]*1) + ((self.c[1]*10000))


with open('9.txt', 'r') as f:
    instructions = f.read().splitlines()

hundred = ["." for _ in range(50)]

grid = [hundred.copy() for _ in range(50)]




hloc = cord((0,0))
lastloc = cord((0,0))
tloc = [cord((0,0)) for _ in range(9)]
d = {'U':cord((1,0)), 'D':cord((-1,0)), 'L':cord((0,-1)), 'R':cord((0,1))}
cords = {tloc[8]}
for i in instructions:
    direct, amount = i.split(' ')
    for j in range(int(amount)):
        lastloc = hloc
        hloc += d[direct]
        
        if not hloc.in_square(tloc[0]):
            tloc[0] = hloc - d[direct]
        for k in range(8):
            if not tloc[k].in_square(tloc[k+1]):
                #tloc[k+1] = tloc[k] - d[direct]
                tloc[k+1] += tloc[k+1].move(tloc[k])
                #if not tloc[k].in_square(tloc[k+1]):
                    #print("BAD REALLY BAD")
        cords.add(tloc[8])
    tmpgrid = [hundred.copy() for _ in range(50)]
    #print(len(tloc))
    #for y, x in enumerate(tloc):
    #    tmpgrid[x.c[0]+16][x.c[1]+20] = str(y)

    #for x in reversed(tmpgrid):
    #    print(''.join(x))


#for i in cords:
#    grid[i.c[0]+16][i.c[1]+20] = '#'

#for i in reversed(grid):
#    print(''.join(i))

print(len(cords))


