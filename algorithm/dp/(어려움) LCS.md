# 문제: LCS
https://www.acmicpc.net/problem/9251  
풀이가 바로 떠오르지 않은 dp 문제  
```
1. 완탐 문제 인가 했지만, 중복되는 부분이 있었고, 시간이 매우 오래 걸리기 떄문에, dp 문제 임을 알았다.  
2. 바텀업 방식 + 2중 배열로 풀어야 겠다는 생각을 했다.
3. s1, s2 문자열을 하나씩 늘려가며, 규칙을 찾고 점화식을 세팅하였다.

# 점화식

   1) s1[n] == s2[m]
      d[n][m] = d[n-1][m-1] + 1
      
   2) s1[n] != s2[m]
      d[n][m] = max(d[n-1][m], d[n][m-1])
```

![image](https://user-images.githubusercontent.com/87055456/141963591-9009ca41-c7de-4b25-83f2-4be2f1841970.png)
# 풀이: 


``` python

s1 = ' '+ input() # ACAYKP
s2 = ' '+ input() # CAPCAK

n , m = len(s1), len(s2)
d = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, n): # ACAYKP
    for j in range(1, m): # CAPCAK
        if s1[i] == s2[j]:
            d[i][j] = d[i-1][j-1] + 1
        elif s1[i] != s2[j]:
            d[i][j] = max(d[i][j-1], d[i-1][j])

print(d[n-1][m-1])

```
