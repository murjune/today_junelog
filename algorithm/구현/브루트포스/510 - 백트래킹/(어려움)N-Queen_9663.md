# 문제:N-Queen - (1)
https://www.acmicpc.net/problem/9663. 

```
엄청 유명한 백트래킹 문제라고한다.
파이썬으로 풀면 시간초과가 계속 뜬다..  
2차원배열을 1차원배열로 생각해서 풀어야한다.  
다른 사람 풀이를 참고해서 풀었다.
```
``` python


import sys
input = lambda : sys.stdin.readline().rstrip()


# 퀸 놓을 수 있는지 가능한지 보는 함수

def possible(x): # x는 몇번째 퀸
    for i in range(x):
        # 같은 y축 or 대각선일때는 공격가능
        if graph[i] == graph[x] or (abs(graph[i] - graph[x]) == abs(x-i)) :
            return False
    return True


# Q 수 구하는 함수식
def Queen(x):
    global result

    if x == n:
        result += 1

    else:
        for i in range(n):
            graph[x] = i
            if possible(x) == True:
                Queen(x + 1) # 다음 퀸

# 출력
n = int(input())
# 각 x축에 q이 하나씩 들어가야 하므로 , y축만 신경쓰면 된다

graph = [0] * n   # y축 정보
result = 0
Queen(0)
print(result)




```
