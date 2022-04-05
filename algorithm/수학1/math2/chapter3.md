# 피보나치 수 풀이 알고리즘 
- 재귀적 구성을 통한 구현 -O(2<sup>n</sup>)  
- dp를 통한 구현 -O(N)
- [피보나치수](https://www.acmicpc.net/problem/2747) : 정수 타입 - int 
- [피보나치수2](https://www.acmicpc.net/problem/2748) : 정수 타입 - long long(F<sub>90</sub> 이 int범위 벗어남,파이썬은 상관없음)
```python
import sys
read = lambda : sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x)+ "\n")

n = int(input())
fibo = [0]*(n+1)
fibo[1] = 1
fibo[2] = 1

for i in range(3,n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

write(fibo[n])
```
# [피사노주기](https://www.acmicpc.net/problem/9471)
피보나치 수를 K로 나눈 나머지는 주기를 갖는데, 이것을 `피사노 주기`라고 한다.  
- e. 3으로 나누었을 때의 피사노주기는 8이다.  
- M = 10<sup>k</sup> 일 때, k > 2라면 주기는 항상 `15 x 10<sup>k-1</sup>`
<img  width = "700" src=https://user-images.githubusercontent.com/87055456/161816672-4b8c72ae-6e08-4e0d-8425-16f85e66e91a.png>   

## [피보나치수 3](https://www.acmicpc.net/problem/2747)  

O(N)의 알고리즘으로는 해결할 수 없다. 따라서, 피사노 주기를 사용해서 피보나치 수를 구해보자!!  
- n은 1,000,000,000,000,000,000보다 작거나 같은 자연수  
- n번째 피보나치 수를 1,000,000으로 나눈 나머지를 출력  
- 피사노 주기를 이용해서 주기를 찾고 문제를 풀 수 있다.  
- 주기의 길이가 K이면, N번째 피보나치 수를 M으로 나눈 나머지는 `n%k`번째 피보나치 수와 같다.  
- M = 10<sup>k</sup> 일 때, k > 2라면 주기는 항상 `15 x 10<sup>k-1</sup>` 
```python

import sys
read = lambda : sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x)+ "\n")

n = int(input())
MOD = 1_000_000
P = MOD * 15 // 10 # 피사노 주기
cycle = 0

fibo = [0]*(P+1)
fibo[1] = 1
fibo[2] = 1

for i in range(3,P+1):
    fibo[i] = (fibo[i-1] % MOD + fibo[i-2] % MOD) % MOD

write(fibo[n%P])
```
- 이번에는 피사노 주기가  `15 x 10<sup>k-1</sup>` 이라는 사실을 모른다고 가정하고 문제를 풀어보자!
# 피보나치 수
<img  width = "700" src="https://user-images.githubusercontent.com/87055456/161807165-05c46cbe-2636-4ff6-b310-2478c62c24b8.png">  


- [증명 과정 : 블로그](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=yh6613&logNo=220466353281)  
- 시간복잡도 : O(logn)  

> 직접 종이에 써서 증명해보자

# 개선된 방법 1 : 행렬의 제곱-(O(logn))

# 개선된 방법 2 : 분할정복기법-((O(logn)))
