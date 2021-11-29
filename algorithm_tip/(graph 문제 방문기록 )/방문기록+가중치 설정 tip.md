# 방문기록 표기할 때 꿀팁

dfs, bfs 문제를 풀 때 정점이 v개 일때, 정점의 방문기록을 다음과 같이 표기할 수 있다. 
``` python
n = 10
visited = [False] * (n+1) 
```

# 방문기록과 가중치(한가지 종류 일 때)

그러나, visted에 방문기록 뿐 아니라 가중치 값 까지 표기할 수 있다.

bfs 예제 문제:  
```
이동 방법: N+1 ,NX2 
이동하는데 걸리는 시간: 1
2에서 15이 되는데 걸리는 최소 시간은??
```
## 풀이 1 : 미 방문한 곳을 0으로 표기하였을 때 
``` python

Max = 100
visited = [False] * (Max+1)

from collections import deque
q = deque([2])
k = 10

while q:
    x = q.popleft()
    if x == k:
        print(visited[k]) 
        break
    for i in (x+1, 2*x):
        if 0 <= i <= Max and visited[i] == 0 : # 방문을 안했을 때, 범위 안에 있을 때
            visited[i] = visited[x] + 1  # 가중치를 표기
            q.append(i)


# 정답 3
```
## 풀이 2 :(그냥 이 풀이법을 암기하자) 미 방문한 곳을 -1라 표기 and 정점의 방문기록은 0으로 표기
``` python
n = 2
Max = 100
visited = [-1] * (Max+1)
visited[n] = 0
# bfs 풀이를 한다고 가정할 때

from collections import deque
q = deque([n])
k = 10

while q:
    x = q.popleft()
    if x == k:
        print(visited[k])
        break
    for i in (x+1, 2*x):
        if 0 <= i <= Max and visited[i] == -1:
            visited[i] = visited[x] + 1
            q.append(i)
            
# 정답: 3
```
# 방문기록과 가중치(0-1BFS 알고리즘)

가중치의 종류가 한가지가 아닐 경우

bfs 예제 문제:  
```
이동 방법: N+1 ,NX2 
이동하는데 걸리는 시간: +1은 1 , *2는 0
2에서 10이 되는데 걸리는 최소 시간은??
``` 

## 풀이 1: 미 방문한 곳을 0으로 표기하였을 때

보통 2가지 정도로 푸는데 

1. visted(방문기록) 배열 따로 time(가중치) 배열 따로 설정
``` python
n,k = map(int,input().split()) # 2 15
Max = 100
visited = [False] * (Max+1)
time = [0]* (Max+1)

from collections import deque
q = deque([n])
visited[n] = True
while q:
    x = q.popleft()
    if x == k:
        print(time[k])
        break

    for i in (x+1, 2*x):
        if 0 <= i <= Max and visited[i] == 0 : # 범위부터 신경 쓰고, 방문기록을 신경써야 한다!! 주의
            if i == x+1:
                visited[i] = True
                time[i] = time[x] + 1
                q.append(i)
            if i == 2*x:
                visited[i] = True
                time[i] = time[x]
                q.appendleft(i)

```
2. visted 배열 안에 (vist, time)을 넣는 방식
``` python

```
## 풀이 2 : (그냥 이 풀이법을 암기하자) 미 방문한 곳을 -1라 표기 and 정점의 방문기록은 0으로 표기  

범위부터 신경 쓰고, 방문기록을 신경써야 한다!! 주의
``` python
n,k = map(int,input().split()) # 2 15
Max = 100
visited = [-1] * (Max+1)
visited[n] = 0

# bfs 풀이를 한다고 가정할 때

from collections import deque
q = deque([n])


while q:
    x = q.popleft()
    if x == k:
        print(visited[k])
        break
    for i in (x+1, 2*x):
        if 0 <= i <= Max and visited[i] == -1 : # 범위부터 신경 쓰고, 방문기록을 신경써야 한다!! 주의
            if i == x+1:
                visited[i] = visited[x] + 1
                q.append(i)
            if i == 2*x:
                visited[i] = visited[x]
                q.appendleft(i)

# 정답 3
```
