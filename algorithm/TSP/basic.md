# [외판원 순회](https://www.acmicpc.net/problem/2098)
```python
import sys

input = lambda: sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x) + "\n")

def travel(v, visited):
    # n= 5, 100000(2) - 1 =  11111(2)
    # 즉, 모든 곳을 방문했다면
    if visited == (1 << n) - 1:
        # 경로가 있을 경우
        if graph[v][0] : return graph[v][0]
        # 경로가 없을 경우
        return INF

    # dp
    if d[v][visited] != INF : return d[v][visited]

    for i in range(1,n): # 모든 도시 순회
        # i를 방문한적이 없는 경우,v-i 경로가 있을 경우
        if not (visited & (1 << i)) and graph[v][i]:
            # 점화식
            d[v][visited] = min(d[v][visited], travel(i, visited | (1 << i)) + graph[v][i])

    return d[v][visited]

# 항상 순회할 수 있는 경우만 주어짐
INF = int(1e9)
n = int(input())  # n은 16이하
d = [[INF] * (1 << n) for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
print(travel(0,1))
```
