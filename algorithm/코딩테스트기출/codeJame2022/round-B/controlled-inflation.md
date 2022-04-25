# [Controlled Inflation](https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb)
dp문제라는 것을 알아차리기 쉽지 않았지만, dp문제임을 인지하면 쉽게 풀 수 있는 문제였다.  
내가, 아직 실전 경험이 부족해서 대회중에는 못 풀었던 것 같다...  
좀 더 긴 영어 문제에 익숙해질 필요가 있다.
# 풀이
정렬 + 그리디 + 다이나믹 프로그래밍  

일단 이 문제의 모든 경우를 고려하게 되면 O(p^n)이라는 무시무시한 시간복잡도를 가지게 된다..  
여기서, 나는 O(p^n)는 정말 말도 안된다고 생각하고, i번째 손님이 요구하는 제품들의 pressure의 min값과 max값을 갖는 두 제품을 s,e로 나누었다.(그 사이 중간값들은 무시해줘도 좋다)  
그렇게 시간 복잡도를 O(2^n)까지 줄이게 되었고, 작은 문제로 쪼개서 푸는 dp기법을 생각하게 되었다.  
> 아니 어제는 왜 dp로 풀면 정당성을 해친다고 생각을 했는지.. 바보같다.(아마 1번문제 풀다가 멘탈이 나가서 그런것같음)  
그래서, 다음과 같이 케이스를 분류하여 점화식을 세웠다.  
- `d[n][0] : n번째 손님의 제품중 min값을 갖는 제품을 가장 마지막에 pressure를 넣는다.`   
- `d[n][1] : n번째 손님의 제품중 max값을 갖는 제품을 가장 마지막에 pressure를 넣는다.:`  

여기서, 또 다시 2가지 경우로 케이스를 나눠주어야 한다.   
- tmp, tmp2 : n-1번째 손님의 제품군의 min값, max값
- s, e : n번째 손님의 제품군의 min값, max값. 
- l = e -s
- d[n-1][0] : 이전 손님의 제품 처리한 마지막 제품이 tmp이고, n-1 번까지의 최소비용은 d[n-1][0]이다.  
- d[n-1][1] : 이전 손님의 제품 처리한 마지막 제품이 tmp2이고, n-1 번까지의 최소비용은 d[n-1][1]이다.  
- d[n][0] = min(tmp(시작점) -> s(끝점)까지의 비용, tmp2(시작점) -> s(끝점)까지의 비용)  
- d[n][1] = min(tmp(시작점) -> e(끝점)까지의 비용, tmp2(시작점) -> e(끝점)까지의 비용)
- `d[n][0] = l +min(abs(e-tmp) + d[n-1][0], abs(e - tmp2) + d[n-1][1])`  
- `d[n][1] = l +min(abs(s-tmp) + d[n-1][0], abs(s - tmp2)+ d[n-1][1])` 

머리에 있는 내용을 풀어 쓰려니 쉽지 않다.  
> 나만 알아보면 됐지..
```python
import sys
input = lambda : sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x)+"\n")

for t in range(int(input())):
    n , p = map(int,input().split())
    d = [[0,0] for _ in range(n+1)]
    tmp ,tmp2= 0, 0
    for i in range(1,n+1):
        arr = sorted(list(map(int,input().split())))
        s,e = arr[0], arr[-1]
        
        d[i][0] =  (e-s)+min(abs(e-tmp) + d[i-1][0], abs(e - tmp2) + d[i-1][1])
        
        d[i][1] = (e-s)+min(abs(s-tmp) + d[i-1][0], abs(s - tmp2)+ d[i-1][1])

        tmp, tmp2 = s, e

    ans = min(d[n])
    write("Case #{0}: {1}".format(t+1, ans))
```
