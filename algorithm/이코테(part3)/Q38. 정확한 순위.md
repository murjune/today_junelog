# 문제: 정확한 순위 - 이코테 책 p 386

플로이드 워셜 알고리즘 문제

# 풀이
```
a-> b로 도달이 가능하다는 것은 a가 b보다 성적이 낮다는 것을 뜻한다.  
따라서, 성적이 낮은 a가 성적이 높은 b를 가리키는 방향 그래프로 나타낼 수 있으므로, 최단 경로 알고리즘을 
수행할 수 있게 된다.

ex) x번 학생의 성적을 확정하기 위해서는
a-> x의 개수(a는 x보다 성적이 낮다) + x -> b(x는 b보다 성적이 높다) 의 개수 합이 v-1 개여야 한다.

즉, 한 노드가 모든 지점의 노드와 연결이 되있다면, 확정된 성적 순위를 알 수 있다는 것이다.  

v 의 최대 범위가 500이기 때문에. '플로이드 워셜' 알고리즘을 수행한 후
모든 노드에 대해서 다른 모든 노드와 연결이 되어있는지 체크하여 문제를 해결한다. 
```
```
예시 입력 1
6 6
1 5
3 4
4 2
4 6
5 2
5 4
예시 출력1
1
```

``` python
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF]* n for _ in range(n)]


# 간선의 정보를 기입
for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1 # a < b 를 의미한다.

# 자기 자신은 0으로 초기화
for i in range(n):
    graph[i][i] = 0


# 플로이드 워셜 알고리즘 - O(n^3) 모든지점에서 모든 지점까지의 거리 탐색

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 확정된 순위의 학생 수 세기
# 한 노드가 모든 지점의 노드와 연결이 되있다면, 확정된 성적 순위를 알 수 있다.
ans = [0]*n

for i in range(n):
    for j in range(n):
        if 0 < graph[i][j] < INF: # i < j 를 의미
            ans[i] += 1
            ans[j] += 1

cnt = 0
for i in ans:
    if i == n-1:
        cnt +=1
print(ans)
```
