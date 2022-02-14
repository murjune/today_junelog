# 문제: [Shortest Reach in a Graph](https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs)

# 풀이
```python
from collections import deque
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = [[] for _ in range(n)]
    
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        x-=1
        y-=1
        graph[x].append(y)
        graph[y].append(x)
        
    s = int(input()) - 1 
    visitied = [-1] * n
    visitied[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for next_c in graph[x]:
            if visitied[next_c] == -1:
                visitied[next_c] = visitied[x] + 6
                q.append(next_c)
    
    ans = []
    for i in range(n):
        if i == s:
            continue
        ans.append(visitied[i])
    
    print(' '.join(map(str, ans)))
        
            
            



```
