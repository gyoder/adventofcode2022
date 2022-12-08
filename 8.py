import math
with open('8.txt', 'r') as f:
    tree_grid = f.read().splitlines()

for i in range(len(tree_grid)):
    tree_grid[i] = [*tree_grid[i]]

for a in range(len(tree_grid)):
    for b in range(len(tree_grid[0])):
        tree_grid[a][b] = int(tree_grid[a][b])
total = 0
map = []
score = 0
for i in range(len(tree_grid)):
    _ = []
    for j in range(len(tree_grid[0])):
        visable = 4
        cur_score = 1
        # go up
        for y in reversed(range(0, i)):
            if tree_grid[y][j] >= tree_grid[i][j]:
                visable -= 1
                cur_score *= abs(i-y)
                break
        else:
            cur_score *= i
        # print(cur_score)
        # down
        for y in range(i+1, len(tree_grid)):
            if tree_grid[y][j] >= tree_grid[i][j]:
                cur_score *= abs(i-y)
                visable -= 1
                break
        else:
            cur_score *= len(tree_grid) - i - 1
        # print(cur_score)
        # left
        for x in reversed(range(0, j)):
            if tree_grid[i][x] >= tree_grid[i][j]:
                cur_score *= abs(j-x)
                visable -= 1
                break
        else:
            cur_score *= j
        # print(cur_score)
        # right
        for x in range(j+1, len(tree_grid[0])):
            if tree_grid[i][x] >= tree_grid[i][j]:
                cur_score *= abs(j-x)
                visable -= 1
                break
        else:
            cur_score *= len(tree_grid[0]) - j - 1
        # print(cur_score)
        if visable > 0:
            total += 1
        _.append([tree_grid[i][j], cur_score])
        if cur_score > score:
            score = cur_score
    map.append(_)


# print(total)
#[print(x) for x in map]
print(score)
