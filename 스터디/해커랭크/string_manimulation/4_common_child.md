[참고 블로그](https://myjamong.tistory.com/317)  

---
# 풀이 1 : pypy3으로 제출해야 정답처리됩니다 :D 
- 시간복잡도 : O(N^2), 공간복잡도 : O(N^2)  
- 같은 알파벳인 경우 : 해당 위치(i,j)에서는 글자를 추가하기 전(i-1,j-1)의 LCS 값보다 1을 더해서 저장한다  
- 만약 알파벳이 다른 경우 : 이전까지 비교한 값중 최대값(max(d[i-1][j], d[i][j-1]))
```python
def commonChild(s1, s2):
    # Write your code here
    d = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(1, n): # ACAYKP
        for j in range(1, m): # CAPCAK
            if s1[i] == s2[j]:
                d[i][j] = d[i-1][j-1] + 1
            elif s1[i] != s2[j]:
                d[i][j] = max(d[i][j-1], d[i-1][j])
    
    return d[n-1][m-1]
```
---
# 풀이 2 : python3으로 제출해도 정답입니다
- 시간복잡도 : O(N^2), 공간복잡도 : O(N). 

<img width= "300" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcrVjs9%2Fbtrh8CowQGJ%2FBkvYwPNpNAR7L7KjwhkBA1%2Fimg.png">  
[출처]:(https://myjamong.tistory.com/317)  

알파벳 하나를 기준으로 1차원 배열(d)을 만들어주고, 같은 글자를 만날 경우 누적 값(cnt)에서 1을 더한 값을 d에 갱신해준다.
순회할 때마다 누적값을 저장할 변수(cnt)를 하나 사용하고, 다른 글자를 만날 경우 cnt 값이 해당 위치의 값보다 작은 경우 해당 값으로 cnt값을 갱신해준다.
이와 같이 cnt에는 이전 위치까지의 lcs값이 계속해서 저장된다.

```python
def commonChild(s1, s2):
    # Write your code here
    n, m = len(s1), len(s2)
    d = [0] * (5000)

    for i in range(n):
        cnt = 0
        for j in range(m):
            
            if cnt < d[j]:
                cnt = d[j]

            elif s1[i] == s2[j]:
                d[j] = cnt + 1
    return max(d)
```
