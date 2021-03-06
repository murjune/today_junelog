# Intro  
현실세계에서는 다양한 문제가 존재한다.  
최적의 해를 구하기에는 시간이 매우 많이 필요하거나  
메모리 공간이 매우 많이 필요한 경우에는 컴퓨터로도  해결하기 힘들다.  
컴퓨터에도 연산속도에 한계가 있고, 메모리 공간을 사용할 수 있는 데이터 개수도 한정적이라는 제약이 발생한다.  
따라서, 우리는 연산속도(시간)과 메모리 공간을 최대한 효율적으로 활용할 수 있는 알고리즘을 구현해내야한다.  

알고리즘 문제들은 각 문제마다 시간제한과 메모리 제한이 걸려있는 종의 최적의 해를 구하는 문제다.  
이때, 어떤 문제는 메모리 공간을 조금 더 사용하면 시간복잡도를 현저히 줄일 수 있는데  

그 대표적인 알고리즘이 바로 다이나믹 프로그래밍(Dynamic Programming)이다.


# 다이나믹 프로그래밍(dp)
다이나믹 프로그래밍, 일명 dp는 메모리를 적절히 사용해서, 시간복잡도를 줄이는 알고리즘 기법입니다.(일종의 트레이드 오프)  

- 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다.  
- dp의 구현은 일반적으로 탑다운 방식과 바텀업 방식으로 구성된다.  

즉, dp알고리즘은 한 번 해결해서 푼 문제를 저장(cashing)해두고, 똑같은문제를 만나면 저장되어 있던 값을 불러오는 것입니다.

이번 포스팅에서는 dp의 대표적인 문제인 피보나치 수열에대해 설명하며 dp를 설명하도록하겠습니다.

# 다이나믹 프로그래밍의 조건

다이나믹 프로그래밍은 문제가 다음 조건을 만족할 때 사용할 수 있습니다.  
```
1. 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제들의 답을 모았을 때 큰 문제의 답이 된다.  
2. 동일한 작은 문제를 반복적으로 해결해야 합니다.(Overlapping Subproblem)  

따라서, 점화식을 세팅해서 dp문제를 푸는 것입니다 :D
```


# 예제) 피보나치 수열  

점화식: 인접한 항들 사이의 관계식을 의미한다.  
피보나치 수열을 점화식으로 표현하면 다음과 같다.

- An = A(n-1) + A(n-2) , A1 =1, A2 = 1
``` python
# 피보나치 수 - 재귀적 구성

def fibo(x):
    if x == 1 or x == 2 :
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4)) # 3
```
그러나, 피보나치 수열의 소스코드를 위와 같이 작성하면, x의 크기가 커질 수록 시간이 기하급수적으로 늘어난다.(시간 복잡도: O(2^n))  
``` python
# 피보나치 수 - 재귀적 구성

def fibo(x):
    print('f('+str(x)+')', end = ' ')
    if x == 1 or x == 2 :
        return 1
    return fibo(x-1) + fibo(x-2)

fibo(6)
# f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(2) f(1) f(4) f(3) f(2) f(1) f(2)    -> 중복되는 경우가 있다.


```
이제 dp의 탑 다운 방식(재귀호출)인 메모리제이션을 통해 피보나치 수열을 구할 경우를 보자.(시간 복잡도: O(N))

``` python
# 피보나치 수 - 재귀적 구성
d = [0] * 101
d[1] = 1
d[2] = 1
def fibo(x):
    print('f('+str(x)+')', end = ' ')
    if d[x] != 0: # 방문한 적이 있다면 return
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(6))# f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4) 8

```
바텀 업(반복문)
```python

n = 100
fibo = [0] * 101
fibo[1] = 1
fibo[2] = 1

for i in range(3,101):

    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[6]) # 8
```

# 탑 다운 vs 바텀 업

- 탑 다운 방식: 큰 문제를 해결하기 위해 작은 문제들을 재귀적으로 호출하는 방식  - 메모리제이션 사용  

- 바텀 업 방식: 작은 문제를 하나씩 해결해 나가면서 먼저 해결했던 작은 문제를 활용해서 그 다음 큰 문제를 순차적으로 해결(반복문 사용) - dp테이블(결과 저장용 리스트) 사용  

dp의 전형적인 형태는 바텀업 방식입니다.  
```
가능하다면 바텀업 방식으로 구현하는 것이 좋다.  
시스템상 재귀함수의 스택 크기가 한정되어 있기 떄문이다. (오버헤드 발생할 수 도..)  
  - 이경우 sys라이브러리의 setrecursion() 함수 호출하여 재귀 완화할 수 있다.
따라서, 반복문을 이용한 바텀업 방식의 dp가 더 성능이 좋다.
```
# 메모리제이션 (탑다운 방식)
- 메모이제이션은 dp를 구현하는 방법중 하나입니다.(dp에 국한된 개념 X)
- 한 번 계산한 결과를 메모리 공간에 메모하는 기법입니다.  
  > 같은 문제를 만나면, 저장했던 결과 불러옴  
  > 값을 기록해 놓는 다는 점에서 Caching이라고도 합니다.  

# dp풀이팁

정리하면 dp는 큰문제를 작은 문제로 나누고, 같은 문제를 한번씩만 풀어 큰 문제를 푸는 효율적인 알고리즘이다.  
이때, 큰 문제를 작은 문제로 나누고 합치는 분할정복 알고리즘과 헷갈릴 수 있는데
dp는 작은 문제들이 서로 영향을 미치지만, 분할정복은 작은 문제들끼리 서로 영향을 끼치지 않는다.(ex. 이분탐색,퀵소트,머지소트)  

또한, 주어진 문제가 dp문제임을 파악하는 것이 은근 어려운데, 특정 문제를 완전 탐색알고리즘으로  
접근했는데, 시간복잡도가 너무 크면 그리디or dp알고리즘을 적용할 수 있는지 확인해보자 :D  
만약, 해결하고자 하는 문제의 서브문제들이 서로 중복된다면 dp문제다!  

(재귀함수로 이미 비효율적인 프로그램을 작성한 후, 작은 문제를 큰 문제에 적용할 수 있다면(= 메모이제이션 기법)  
탑다운 방식으로 코드를 고치는 방법도 있다.)






