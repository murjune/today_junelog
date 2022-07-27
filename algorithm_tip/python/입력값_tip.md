국영수 문제와 같이 입력값을 여러개 받아 list에 저장할 때 간략하게 표현할 수 있다.  
국영수 문제: https://github.com/murjune/today_junelog/blob/main/algorithm/%EC%A0%95%EB%A0%AC/%EA%B5%AD%EC%98%81%EC%88%98_10825.md

# 예시
``` python

# 입력
n = 3
arr = []

for _ in range(n):
    name, age, height, hobby = input().split()
    arr.append([name, int(age), int(height), hobby])

print(arr)
```

```
# 입력값
이준원 25 181 헬스
양재윤 24 167 낮잠
김기재 25 170 드라마시청

# 출력값
[['이준원', 25, 181, '헬스'], ['양재윤', 24, 167, '낮잠'], ['김기재', 25, 170, '드라마시청']]
```
