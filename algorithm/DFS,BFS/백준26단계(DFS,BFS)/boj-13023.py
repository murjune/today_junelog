# https://velog.io/@murjune/%EB%B0%B1%EC%A4%80-ABCDEfeat.Python
import sys
input = lambda : sys.stdin.readline().rstrip()

def dfs(x,cnt): #O(V+E)
    if cnt == GOAL:
        print(1)
        exit()
    for u in graph[x]:
        if not visited[u]:
            visited[u] = True
            dfs(u,cnt+1)
            visited[u] = False

if __name__ == '__main__':
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    GOAL = 5
    visited = [False] * v
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(v): # O(V)
        visited[i] = True
        dfs(i,1)
        visited[i] = False

    print(0)
