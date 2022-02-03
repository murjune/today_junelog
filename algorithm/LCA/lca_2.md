# [LCA 2](https://www.acmicpc.net/problem/11438)

# 풀이
```python
import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)
LOG = 21 # 2^20 = 100만 ,데이터가  100만개까지 들어온다고 가정

# LCA 2(최소 공통 조상 찾기)
n = int(input())

# 노드의 부모 테이블
parent = [[0]*LOG for _ in range(n+1)]
# 노드의 깊이 테이블
depth = [0] * (n+1)
# dfs 방문 체크 테이블
visited = [False]*(n+1)

# 노드 들의 간선 정보
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1. dfs함수를 통해 depth + parent[x][0] 테이블 갱신
def dfs(x ,d): # 시작은 root 노드, d = 0

    visited[x] = True

    for i in graph[x]: # x의 자식 노드들
        if not visited[i]:  # 방문한 노드가 아닐 경우
            parent[i][0] = x # i의 한 칸 위의 부모만 기록
            depth[i] = d+1
            dfs(i,d+1) # 깊이 1추가

    return
# 2. 모든 부모 노드 세팅하기 - DP

def set_parent():
    dfs(1,0) # 루트 노드 1번
    for i in range(1,LOG):
        for j in range(1,1+n):
            # bottom - up 방식
            # ex) 1은 2의 부모 , 2는 5의 부모
            #  5의 2칸 위 부모 = (5의 1칸 위 부모)의 1칸위 부모
            # 즉, 할아버지 = 아버지의 아버지
            # 증조할아버지 = 할아버지의 아버지
            parent[j][i] = parent[parent[j][i-1]][i-1]

# 3. 두 정점의 LCA 찾기
def lca(a,b):

    # 1. 두 노드의 깊이 맞추기
    # b를 더 깊이 설정
    if depth[a] > depth[b]:
        a ,b = b,a
    # 더 큰 값 b 점프 -> 깊이 맞추기
    for i in range(LOG-1,-1,-1): # LOG-1~0
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i] # b는 b의  2^i번째 부모로 change

    # 2. 부모가 같아 질 때까지, 부모 방향으로 올라가기

    if a == b: return a
    # 2-1. 두 노드를 기준으로 가장 멀리 있는 부모부터 계산해 부모가 동일하지 않는 시점을 찾는다.
    # 2-2. 부모가 동일 하지 않은 만큼 점프를 한다.
    # 2-3. 2-1과 2-2과정 반복
    # 2-4. loop를 마친 후, 정점의 1칸 위가 LCA이다.
    for i in range(LOG-1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]




# 출력
set_parent()
m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))

```
