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
    if d[v][visited] != -1 : return d[v][visited]

    # 초깃값 세팅
    d[v][visited] = INF

    for next in range(1,n): # 모든 도시 순회
        # 다음 방문도시 != 현재 도시,i를 방문한적이 없는 경우,v-i 경로가 있을 경우
        if next != v and not (visited & (1 << next)) and graph[v][next]:
            # 점화식
            d[v][visited] = min(d[v][visited], travel(next, visited | (1 << next)) + graph[v][next])

    return d[v][visited]

# 항상 순회할 수 있는 경우만 주어짐
INF = int(1e9)
n = int(input())  # n은 16이하
d = [[-1] * (1 << n) for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
print(travel(0,1))
```
