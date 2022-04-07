# [이항 계수 1](https://www.acmicpc.net/problem/11050)
- n개중 k 개를 순서없이 고르는 방법: <sub>n</sub>C<sub>k</sub>  
그러나 10! = 3628800 으로 약 300만이고, n의 수가 증가할 수록 급격하게 수가 증가하게 된다.  
> 참고로 O(n!)이 가장 안좋은 효율을 가진 시간복잡도 중 하나이다.  

따라서, 이를 해결하고자 `파스칼 삼각형`이라는 방법을 사용할 수 있다. 

# 파스칼 삼각형
<img width = "500" src ="https://user-images.githubusercontent.com/87055456/162268993-32125143-39f9-450c-a308-23d54a79f324.png">  

- 위의 그림은 6까지의 파스칼 삼각형  
- n행 k열이 <sub>n</sub>C<sub>k</sub>을 나타내는 삼각형을 파스칼 삼각형이라 한다.  
- 이를 구현하려면 2차원 배열을 사용한다, C[n][k] = n번째 줄의 k번째 수  
- C[n][1] = 1, C[n][n] =1   
- C[n][k] = C[n-1][k] + C[n-1][k-1] 로 정의할 수 있다.  
- C[n][k] = C[n][n-k]  
- (1) C[n-1][k] :  n번째 수를 포함하냐 (2) C[n-1][k-1] :  포함안하냐를 기준으로 분할한 것이다.   

# [이항 계수 2](https://www.acmicpc.net/problem/11051)
- 파스칼 삼각형을 이용해 DP로 푸는 문제
```python
n ,k= map(int,input().split())

c = [[-1] *(n+1) for _ in range (n+1)]
MOD =10007
def solve(n,k):
    if k == 0 or k == n : return 1
    if c[n][k] >= 0 : return c[n][k]

    c[n][k] = solve(n-1,k)%10007 + solve(n-1,k-1)%10007
    return c[n][k]%10007
print(solve(n,k))
```
# 나머지 이항계수의 성질들
- n개 중에 k개를 중복없이 뽑는 방법의 수 : <sub>n</sub>C<sub>k</sub>  
- n개 중에 k개를 중복 허용하면서 뽑는 방법의 수(중복 조합) : <sub>n+k-1</sub>C<sub>r</sub>  
- 0과 1로만 이루어진 문자열의 개수 : <sub>n+k</sub>C<sub>k</sub>  
- 0과 1로만 이루어진 문자열의 개수(1은 연속하지 않음, 이친수) : <sub>n+1</sub>C<sub>k</sub> 
- 카탈란 수 <sub>2n</sub>C<sub>n</sub> / n+1

