# [행렬의 덧셈](https://www.acmicpc.net/problem/2738)

두 행렬을 더할 때 O(NM) = O(N<sup>2</sup>)의 시간이 걸린다.
```python
import sys
input = lambda : sys.stdin.readline().rstrip()
n, m  = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
arr2 = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j] += arr2[i][j]

for i in range(n):
    print(' '.join(map(str, arr[i])))
```

# [행렬 곱셈](https://www.acmicpc.net/problem/2740)
두 행렬을 곱할 때 O(NRM) = O(N<sup>3</sup>)의 시간이 걸린다.  
```python

# Test Case
import sys
input = lambda : sys.stdin.readline().rstrip()
n, m  = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

m,k =  map(int,input().split())
arr2 = [list(map(int,input().split())) for _ in range(m)]

arr3 = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for v in range(m):
            arr3[i][j] += arr[i][v] * arr2[v][j]

for i in range(n):
    print(' '.join(map(str, arr3[i])))
```
# [나머지 연산 분배법칙](https://youseokhwan.me/blog/remainder-distribution-property/)

# [행렬 제곱](https://www.acmicpc.net/problem/10830)
제곱수 구할 때와 마찬가지로 A<sup>2n</sup> = (A<sup>n</sup>) * (A<sup>n</sup>)으로 쪼개서 곱한다!  
```python

def mul(a1 ,a2):
    a3 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for v in range(n):
                a3[i][j] += (a1[i][v]%1000 * a2[v][j]%1000) % 1000
                a3[i][j] %= 1000

    return a3

def solve(b):

    if b == 1 : return A

    if b % 2 :
        tmp = solve(b-1)
        ans = mul(tmp, A)
    else:
        tmp = solve(b//2)
        ans = mul(tmp, tmp)
    return ans

# Test Case
import sys
input = lambda : sys.stdin.readline().rstrip()
n, b  = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(n)]

# 요 부분을 빼먹으면 틀림
for i in range(n) :
    for j in range(n):
        A[i][j] %= 1000

ans = solve(b)
# 출력

for i in range(n):
    print(' '.join(map(str, ans[i])))
```
- 주요 반례 케이스  
```
# 입력값
2 1
1000 1000
1000 1000
# 정답
0 0 
0 0
# 오답
1000 1000
1000 1000
```
