# [LCA](https://www.acmicpc.net/problem/11437). -기초문제  

# 풀이
```python
import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)


# LCA(최소 공통 조상 찾기)
n = int(input())

# 노드의 부모 테이블
parent = [0]*(n+1)
# 노드의 깊이 테이블
depth = [0]* (n+1)
# dfs 방문 체크 테이블
visited = [False]*(n+1)

# 노드 들의 간선 정보
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1. dfs함수를 통해 depth + parent 테이블 갱신
def dfs(x ,d): # 시작은 root 노드, d = 0

    visited[x] = True

    for i in graph[x]: # x의 자식 노드들
        if not visited[i]:  # 방문한 노드가 아닐 경우
            parent[i] = x # i의 부모 check
            depth[i] = d+1
            dfs(i,d+1) # 깊이 1추가

    return

# 2. 두 정점의 LCA 찾기
def lca(a,b):

    # 2-1. 두 노드의 깊이 맞추기
    while depth[a] != depth[b]:
        # 깊이가 더 깊은 쪽 -> 1레벨씩 올라가기
        if depth[a] > depth[b]:
            a = parent[a]
        elif depth[a] < depth[b]:
            b = parent[b]
    # 2-2. 부모가 같아 질 때까지, 부모방향으로 거슬러 올라가기

    while a != b:
        a = parent[a]
        b = parent[b]

    # lca 반환
    return a
# 출력
dfs(1,0)
m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))

```
