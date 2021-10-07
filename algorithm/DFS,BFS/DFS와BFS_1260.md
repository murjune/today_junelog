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


# 입력1

n, m, v = map(int, input().split())
# n: 정점의 개수 m: 간선 개수, v: 탐색 시작 번호


# 입력2
# 간선이 연결하는 두 정점의 번호가 주어 진다.
arr = [list(map(int, input().split())) for _ in range(m)]


# 방문 유무

visted = [False] * (n+1)

# graph (인접행렬 방식) 으로 나타내기

graph = [[] for _ in range(n+1)] # 0번 노드를 비워 두기 위해 n+1
for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in range(len(graph)): # 그래프 정렬
    graph[i].sort()

# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

# 출력 
dfs(graph,v,visted)
print(' '.join(map(str, ans_dfs)))




```
