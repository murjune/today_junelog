문제: DFS와 BFS
https://www.acmicpc.net/problem/1260


``` python
# 조건
# 정점 번호는 1번부터
# 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료

# 입력1

n, m, v = map(int, input().split())
# n: 정점의 개수 m: 간선 개수, v: 탐색 시작 번호
 

# 입력2
# 간선이 연결하는 두 정점의 번호가 주어 진다.
arr = [list(map(int, input().split())) for _ in 
	  range(m)]

print(arr)
# 1 2 1 3 1 4 2 4 3 4 ()

# graph = [[] for _ in range(n+1)]
# # 0번 노드를 비워 두기 위해 n+1

# for _ in range(m):
# 	graph


```
