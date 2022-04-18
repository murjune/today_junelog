[참고 블로그](https://www.weeklyps.com/entry/%ED%94%84%EB%A6%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Prims-algorithm)
---
# MST 알고리즘
- ST : graph -> Tree (그래프에서 일부 간선을 선택해 만든 트리)
- MST : ST 중 선택한 간선의 w의 합이 최소인 tree  

프림 알고리즘은 무향 연결 그래프가 주어질 때, '최소 스패닝 트리' 라고 부르는 서브 그래프를 찾는 알고리즘이다.  
크루스칼 알고리즘과 같이 MST를 찾는 알고리즘이지만, 프림 알고리즘은 공집합에서 정점을 하나씩 추가해나가는 알고리즘이고  
크루스칼 알고리즘은 간선을 하나씩 추가해나가는 알고리즘인 것에서 차이가 있다.  
이는 응용 상황에 따라 두 알고리즘의 효율성이 달라질 수 있기 때문에 둘다 알면 좋다 :D  

## 프림 알고리즘

- 1. 그래프에서 아무 정정를 선택하여 비어있는 T에 포함시킨다. (T는 공집합)
- 2. 선택한 정점(u)과 선택하지 않은 정점(v)를 연결하는 간선 중 최솟값을 찾는다. 이 간선을 (u,v)라고 표기 
- 3. MST에 (u,v)를 추가하고, v를 선택한다.  
- 4. 모든 정점을 선택할 때까지 2,3번 과정을 반복한다.(T == MST -> finish)  

이 방법을 구현해 보겠다.  
### 방법 1 : 배열 구현 O(V^2)
배열을 사용하여, T와 각 노드를 연결하는 최소 w를 찾는 방법
```python
# prim 알고리즘
def prim():

    res = 0
    # 0번 노드 부터 시작
    dist[0] = 0

    # 방문하지 않은 노드 중 가장 가까운 노드 now  찾기
    for _ in range(n): # v의 개수만큼 반복 
        now = -1
        min_dist = INF
        for j in range(n):
            if not visited[j]:
                if min_dist > dist[j]:
                    min_dist = dist[j]
                    now = j

        if now == -1 : return INF # cycle 발생했다는 의미

        visited[now] = True
        T.append(now)
        res += min_dist

        for k in range(n):
            # 아직 방문 x , 현재 dist보다 더 가까운 애 있으면 갱신
            if not visited[k] and graph[now][k] != INF:
                dist[k] = min(dist[k], graph[now][k])

    return res

n = 7
INF = int(1e9)

# graph[i][j] : cost
graph  = [[0, 7, INF, INF, 3, 10, INF],
          [7, 0, 4, 10, 2, 6, INF],
          [INF, 4, 0, 2, INF, INF, INF],
          [INF, 10, 2, 0, INF, 9, 4],
          [3, 2, INF, INF, 0, INF, 5],
          [10, 6, INF, 9, INF, 0, INF],
          [INF, INF, INF, 4, 5, INF, 0]]

dist = [INF] * n # dist[i] : 선택된 노드들과 i 노드가 연결되어 있는 간선의 비용 중 최소비용
visited = [False]* n # 방문 기록
T = [] # 경로

print(prim()) # 21
print(T) # [0, 4, 1, 2, 3, 6, 5]

```
### 방법 2 : 힙으로 구현 O(ElogE)  
모든 간선이 heap을 들어갔다 나오므로 ElogE이다.  

```python
# 개선된 prim 알고리즘
def prim(u = 1):

    import heapq
    res = 0
    hq = []
    heapq.heappush(hq, (0, u)) # 임의의 정점을 선택하여 비어있는 T에 포함시킨다.

    for _ in range(n):
        for cost,v in graph[u]: # 노드 u와 연결된 간선의 비용 중 최소비용이 있는지
            if not visited[v]: # 방문하지 않은 노드
                heapq.heappush(hq,(cost,v)) # O(logE)

        while hq: # hq가 empty면안됨
            
            c,v = heapq.heappop(hq) # O(logE)
            if not visited[v]: # 방문한적 없을 경우, u노드 갱신
                u = v
                res += c
                visited[u] = True
                T.append(u)
                break

    return res

n = 7
INF = int(1e9)

# graph[i][j] : cost
graph = [
                [],
                [(7, 2), (3, 5), (10, 6)],
                [(7, 1), (4, 3), (10, 4), (2, 5), (6, 6)],
                [(4, 2), (2, 4)],
                [(10, 2), (2, 3), (9, 6), (4, 7)],
                [(3, 1), (2, 2), (5, 7)],
                [(10, 1), (6, 2), (9, 4)],
                [(4, 4), (5, 5)]
           ]

visited = [False]* (n+1) # 방문 기록
T = [] # 경로

print(prim()) # 21
print(T) # [1, 5, 2, 3, 4, 7, 6]
```
