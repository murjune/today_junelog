
# 풀이
```python
#!/bin/python3

import math
import os
import random
import re
import sys

def dfs(x):
    global road

    for n_c in graph[x]:
        if not visited[n_c]:
            visited[n_c] = 1
            road += 1
            dfs(n_c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))
        # init
        ans = n * c_lib

        # linked list
        graph = [[] for _ in range(n + 1)]
        for city in cities:
            a, b = city[0], city[1]
            graph[a].append(b)
            graph[b].append(a)

        visited = [0] * (n + 1)
        
        road = 0
        lib = 0

        for city in range(1,n+1):
            if not visited[city]:
                visited[city] = 1
                dfs(city)
                lib += 1

        ans = min(ans, road*c_road + lib * c_lib)

        fptr.write(str(ans) + '\n')

    fptr.close()

```
