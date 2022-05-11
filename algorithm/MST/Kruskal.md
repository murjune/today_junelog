[참고 블로그](https://www.weeklyps.com/entry/%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Kruskals-algorithm#d3)
---
# 신장 트리

신장 트리란 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 뜻한다.  
이때, 모든 노드가 포함되어 서로 연결하면서, 사이클이 존재하지 않는다는 조건은 트리의 성힙 조건이기도 하다.  
![image](https://user-images.githubusercontent.com/87055456/146640802-c1c15799-e3c5-4e73-b428-60d9b73bd05d.png) 

그래서 이런 그래프를 신장 트리라 하는 것이다.  

# 크루스칼 알고리즘

우리는 다양한 문제 상황에서 가능한 한 최소한의 비용으로 신장 트리를 찾아야 할 때가 있다.  
```
ex) N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있도록 하자!

2개의 도시 A,B를 선택했을 때 A-> B로 이동하는 경로가 반드시 존재하도록 도로를 설치하고자 한다.  
모든 도시를 연결할때, 최소한의 비용으로 연결하려면 어떻게 해야할까?
```
대표적인 최소 신장 트리 알고리즘에는 크루스칼 알고리즘이 있다.  
![image](https://user-images.githubusercontent.com/87055456/146640852-a31330cd-f73f-4ac4-9486-a48732e40df7.png)

크루스칼 알고리즘을 사용하면 가장 적은 비용으로 모든 노드를 연결할 수 있는데, 크루스칼 알고리즘은 그리디 알고리즘으로 분류된다.  
먼저, 모든 간선에 대하여 정렬을 한 후, 가장 거리가 짧은 간선부터 집합에 포함시키면 된다.  
이떄! 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않는다.
```
1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 간선이 사이클의 발생 여부를 확인한다.
  1) 사이클 발생: 최소 신장 트리에 포함 X
  2) 사이클 발생 X: 최소 시잔 트리에 포함 ㅇ
3. 모든 간선에 대해 2번을 반복한다.
```  

최소 신장 트리는 일종의 트리 자료구조이기 때문에, 간선의 개수는 V-1개라는 특징이 있다.  

# 크루스칼 알고리즘 소스 코드 및 정리

크루스칼 알고리즘은 간선의 개수가 E개 일때. O(ElogE)의 시간 복잡도를 갖는다.  

왜냐하면, 크루스칼 알고리즘에서 가장 오래걸리는 부분이 간선을 가중치 기준으로 정렬하는 작업이며, E개의 데이터 정렬할 떄 걸리는  
시간 복잡도는 O(ElogE)이기 때문이다.  

크루스칼 내부에서 사용되는 서로소 집합 알고리즘의 시간 복잡도는 정렬 알고리즘의 시간 복잡도보다 작으므로 무시한다.
```
입력 예시
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
# 출력 예시
159
```
``` python



def find(x):
    if parent[x] < 0:
        return x
    # 경로 압축
    y = find(parent[x])
    return y
def Union(x,y):
    x = find(x)
    y = find(y)
    if x == y: # 같은 집합
        return True

    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x

    else:
        parent[y] += parent[x]
        parent[x] = y

    return False

v,e = map(int,input().split())
parent = [-1 for x in range(v+1)]

graph = [tuple(map(int,input().split()))for _ in range(e)]

graph.sort(key =lambda x:x[2])

cost = 0

for (a,b,c) in graph:

    if Union(a,b) == True: # 사이클 발생 ㅇ
        continue
    else: # 사이클 발생 X
        cost += c
print(cost)

```
