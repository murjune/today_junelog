# 피보나치 수 풀이 알고리즘 
- 재귀적 구성을 통한 구현 -O(2<sup>n</sup>)  
- dp를 통한 구현 -O(N)
- [피보나치수](https://www.acmicpc.net/problem/2747) : int 
- [피보나치수2](https://www.acmicpc.net/problem/2748) : long long(파이썬은 상관없음)
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
# 피사노주기
# 피보나치 수
<img  width = "700" src="https://user-images.githubusercontent.com/87055456/161807165-05c46cbe-2636-4ff6-b310-2478c62c24b8.png">  
- [증명 과정 : 블로그](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=yh6613&logNo=220466353281)  
- 시간복잡도 : O(logn)
> 직접 종이에 써서 증명해보자

# 개선된 방법 1 : 행렬의 제곱-(O(logn))

# 개선된 방법 2 : 분할정복기법-((O(logn)))
