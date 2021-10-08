문제: DFS와 BFS
https://www.acmicpc.net/problem/1260

# 조건
```
# 조건
1. 정점 번호는 1번부터
2. 정점 번호가 작은 것을 먼저 방문하고,
3. 더 이상 방문할 수 있는 점이 없는 경우 종료
```
# 풀이
``` python



# dfs 함수
ans_dfs = []  # 경로
def dfs(graph,v, visted):

    if visted[v] == True: # 이미 방문 했으면 잘가~
        return

    visted[v] = True # 방문처리 하기
    ans_dfs.append(v)

    for i in graph[v]: # 다음 경로 검사

        dfs(graph, i, visted)


# bfs 함수
from collections import deque

ans_bfs = []  # 경로
def bfs(graph, v, visted):
    q = deque([v])  # 시작
    visted[v] = True
    while q:  # q가 빌때 까지
        v = q.popleft()

        ans_bfs.append(v)
        # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
        for i in graph[v]:
            if visted[i] == False:  # 방문하지 않았다면

                visted[i] = True  # 방문처리
                q.append(i)


# 입력1

n, m, v = map(int, input().split())
# n: 정점의 개수 m: 간선 개수, v: 탐색 시작 번호


# 입력2
# 간선이 연결하는 두 정점의 번호가 주어 진다.
arr = [list(map(int, input().split())) for _ in range(m)]


# 방문 유무

visted = [False] * (n+1)
visted2 = [False] * (n+1)

# graph 인접행렬 방식으로 나타내기

graph = [[] for _ in range(n+1)]# 0번 노드를 비워 두기 위해 n+1
for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in range(len(graph)): # 그래프 정렬
    graph[i].sort()

# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

dfs(graph, v, visted)
print(' '.join(map(str, ans_dfs)))
bfs(graph, v, visted2)
print(' '.join(map(str, ans_bfs)))




```

## 그래프에 노드의 경로 표시

``` python

arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]# 0번 노드를 비워 두기 위해 n+1
for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
    
```
위 소스코드를 아래와 같이 표현 할 수도 있다.
```python

n = 4
m = 5

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
# N x N 크기 graph

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1 # 노드의 경로 표시

```
