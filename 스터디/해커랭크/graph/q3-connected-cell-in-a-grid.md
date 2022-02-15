# 문제 : [connected-cell-in-a-grid](https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs)
```python
#!/bin/python3

import math
import os
import random
import re
import sys


def dfs(x,y):
    global tmp
    for i in range(8):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if 0<= n_x < n and 0<= n_y < m and graph[n_x][n_y]== 1 and visited[n_x][n_y] == 0 :
            visited[n_x][n_y] = 1
            
            tmp += 1
            dfs(n_x,n_y)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().rstrip().split())))

    # 1
    oneGroup = []
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                oneGroup.append((i,j))

    # 2
    visited = [[0]*(m) for _ in range(n)]
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]

    # solve
    ans = 0
    tmp = 1
    for (i,j) in oneGroup:
        if visited[i][j] == 0:
            visited[i][j] = 1
            dfs(i,j)
            ans = max(ans, tmp)
            tmp = 1

    fptr.write(str(ans) + '\n')

    fptr.close()

```
