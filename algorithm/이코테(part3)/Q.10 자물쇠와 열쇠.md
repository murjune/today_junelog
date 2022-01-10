# 문제: [자물쇠와 열쇠](https://programmers.co.kr/learn/courses/30/lessons/60059)

시뮬레이션 문제 (내가 약점인 부분.. 연습 많이하자)
# 풀이
``` python
from copy import deepcopy

def rotate(arr):
    change = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            change[j][(m-1)-i] =arr[i][j]
    return change

def check(i,j,arr,key):
    for x in range(m):
        for y in range(m):
            if 0<= (x+i) < n and 0<= (y+j) < n:
                if arr[x+i][y+j]== 1 and key[x][y] == 1:
                    return False
                elif arr[x+i][y+j]== 0 and key[x][y] == 1:
                    arr[x+i][y+j] = 1
    
    for i in arr:
        if 0 in i:
            return False
    return True
def move(lock,key):
    # 열쇠와 겹치지 않는 lock부분
    
    for i in range(-(m-1),n):
        for j in range(-(m-1),n):
            arr = deepcopy(lock)
            if check(i,j,arr,key) == True:
                return True
    return False
                            
    # 검사
    for i in arr:
        if 0 in i:
            return False

    return True

def solution(key, lock):
    global m,n
    m = len(key)
    n = len(lock)
    # 회전
    for _ in range(4):
        key = rotate(key)
        # 평행 이동
        if move(lock,key) == True:
            return True
    
    return False
```
