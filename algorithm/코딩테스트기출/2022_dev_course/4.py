import heapq

INF = int(1e9)
def solution(graph: list, c: int):
    start = None
    end = None
    n = len(graph)
    m = len(graph[0])
    distance = [[INF for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (graph[i][j] == 2):
                start = (i, j)
            elif (graph[i][j] == 3):
                end = (i, j)

    dijkstra(n, m, start, end, c, graph, distance)
    answer = distance[end[0]][end[1]]
    return answer

def dijkstra(n, m, start, end, c: int, graph: list, distance: list):
    q = []
    import heapq
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    distance[start[0]][start[1]] = 0  # 자기 자신까지의 거리는 0
    heapq.heappush(q, (0, start[0], start[1]))  # (비용, 노드)

    while q:
        now_cost, x, y = heapq.heappop(q)
        if (x == end[0] and y == end[1]):
            distance[x][y] = now_cost
            break

        if (now_cost > distance[x][y]):
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m):
                if (graph[nx][ny] == 1):
                    next_cost = c + 1
                else:
                    next_cost = 1
                cost = now_cost + next_cost
                if (distance[nx][ny] > cost):
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))