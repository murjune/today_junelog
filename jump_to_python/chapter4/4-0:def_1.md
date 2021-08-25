# def 기초1

#입력값 출력값 둘다 있는 함수
``` python
def sum(a, b):
    result = a + b
    return  result

print(sum(1,2)) # 3
```
#입력값만 있는 함수
```python
def sum(a,b):
    print("{0}과 {1}의 합은 {2}".format(a,b,a+b) )
print(sum(1,3)) # none
```

#출력값만 있는 함수
```python
def tell():
    return "hello"
print(tell() ) # hello
```

#입력값, 출력값 둘다 없는 함수
```python
def say():
    print("hi")

print(say()) # none
```

#예시

#append는 입력값만 있는 함수
```python
a = [1, 2, 3]
print(a.append(4))  # None # append는 return을 해주는 함수가 아니기때문
```
#pop은  입력값 출력값 둘 다 있는 함수
```python
a = [1, 2, 3]
print(a.pop()) # 3
```
