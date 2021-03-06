# 제곱수 구하기

a<sup>b</sup> 구할 때 보통 다음과 같이 총 O(b)라는 시간이 걸리게 된다.  
```python
a, b = 2 , 10
ans = 1

for i in range(b):
    ans *= a

print(ans) # 1024
```
그러나, O(b)보다 더 빠른 방법이 2가지 존재하는데 이에 대해 알아보자!
# 분할정복 

제곱수는 a<sup>2b</sup> 와 a<sup>2b+1</sup>와 같이 제곱수가 짝수/홀수일 때로 나눌 수 있다.  
분할정복 기법을 통해 제곱수를 계속 아래와 같이 등분한 후, 서브 문제들을 계산하면 총 `O(logb)`의 시간으로 해결할 수 있다.
- 짝수 : a<sup>2b</sup> =  a<sup>b</sup> x a<sup>b</sup>
- 홀수 : a<sup>2b + 1</sup> = a<sup>1</sup> x a<sup>b</sup> x a<sup>b</sup>
```
ex) a : 2, b = 27 
a^27 = a x a^13 x a^13
a^13 = a x a^12
a^12 = a^6 x a^6
a^6 = a^3 x a^3
a^3 = a x a^2
a^2 = a x a
```
이를 코드로 나타내보자
```python
# 분할 정복 기법으로 제곱수 구하기!

def solve(a,b):

    if b == 0 : return 1
    if b == 1 : return  a


    if b % 2 == 0: # b가 짝수
        tmp = solve(a, b//2)
        ans = tmp * tmp # ans = solve(a, b//2) * solve(a, b//2) 로 하면 O(b)가 되므로 분할정복이 무의미해진다.
    else: # b가 홀수  
        tmp = solve(a, b//2)
        ans = tmp * tmp * a

    return ans

# Test Case
print(solve(2,0)) # 1
print(solve(2,10)) # 1024
print(solve(3,17)) # 129140163
```
# 이진수의 원리
이진수의 원리를 이용해도 O(logb)의 시간으로 제곱수를 구할 수 있다.  
똑같은 예제로 이진수의 원리에 대해 배워보자~
- a<sup>b</sup> = 2<sup>27</sup>
- 27은 이진수로 11011(2)이다.
- 27 = 2<sup>0</sup> + 2<sup>1</sup> + 2<sup>3</sup> + 2<sup>4</sup>  
- 27 = 1 + 2 + 8 + 16  
- 2<sup>27</sup> = 2<sup>1 + 2 + 8 + 16 </sup>  
- 2<sup>27</sup> = 2<sup>1</sup> x 2<sup>2</sup> x 2<sup>8</sup> x 2<sup>16</sup>. 
- 이를 이용해서 이진수 자리수가 1일 때만 계속해서 a`*`a를 곱해가며 제곱을 구하는 것이다.  

글로 보면 무슨 말인지 알기 어렵다.. 직접 종이에 이 과정을 써가면서 학습하자! 다음은 코드로 나타낸 것이다.  
```python
# 이진수의 기법으로 제곱수 구하기!

def solve(a,b):

    ans = 1

    while (b > 0):

        if (b % 2 == 1):  # 제곱수 b를 이진수로 나타냈을 때 그 자리가 1인 경우
            ans *= a  # ans에 a를 곱해준다.
        a = a*a
        b //= 2

    return ans

# Test Case
print(solve(2,0)) # 1
print(solve(2,10)) # 1024
print(solve(3,17)) # 129140163
```

이해하기 힘들 수 있지만, 다양한 케이스를 직접 종이에 써가며 공부하자 :D
