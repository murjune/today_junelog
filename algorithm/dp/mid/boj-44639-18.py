# https://www.acmicpc.net/board/view/44639
from itertools import permutations


def dfs(x, y, z):
    if x <= 0 and y <= 0 and z <= 0:
        return 0

    if x < 0: x = 0
    if y < 0: y = 0
    if z < 0: z = 0
    if d[x][y][z] < 1000: return d[x][y][z]

    for i, j, k in list(permutations(attack)):
        d[x][y][z] = min(d[x][y][z], dfs(x - i, y - j, z - k) + 1)

    return d[x][y][z]

n = int(input())
arr = list(map(int,input().split()))
if len(arr) == 1:
    print(arr[0]//9 + 1)
    exit()
elif len(arr) == 2:
    arr = arr +[0]

attack = [9, 3, 1]
d = [[[1000]*61 for _ in range(61)] for _ in range(61)]
# d[x][y][z] = min(d[x][y][z], d[x-9][y-6][z-1] + 1)
# 1 3 9
print(dfs(arr[0], arr[1], arr[2]))
