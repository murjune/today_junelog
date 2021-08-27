# chapter4 연습문제

## 1
#방법1
```python
# 1
# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

def is_odd(a):
    if a % 2 == 0:
          print("{0}는 짝수다.".format(a))

    else:
        if a % 2 == 1:
            print("{0}는 홀수다.".format(a))

    

is_odd(2)
is_odd(1)
is_odd(3)

```
#방법2

```python
# lamda
is_odd = lambda a: print("{0}은 짝수다.".format(a)) if a %2 ==0 else  print("{0}은 홀수다.". format(a))

is_odd(1) # 1은 홀수다.
is_odd(2) # 2은 짝수다.
```

## 2 
```python
# 2
# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

def average(*args):
    result = 0
    for i in (args):
        result += i

    result_avr = result / len(args)
    return result_avr

print(average(2,3,4,5,6)) # 4.0


```
## 3 : 너무 쉬워서 생략
```python

```

```python

```

```python

```

```python

```
