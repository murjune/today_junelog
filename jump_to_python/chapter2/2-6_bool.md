# bool

## bool- 예시1
``` python
a = [1, 2, 3, 4]

while a: # a가 []되어 거짓 이 되면 while문에서 조건이 거짓이 되므로 중지 된다.
    print(a.pop())
```
## bool- 예시2
``` python
a = [1, 2, 3, 4]

if [1, 2, 3]: # [1,2,3]이 참이면 "참"아라는 문자열 출력, 그렇지 않으면 "거짓"을 출력
    print("참")
else:
    print("거짓")
# 참
```
## bool 연산
``` python
print(bool([1,2,3])) # True
print(bool([])) # False
print(bool(0)) # False
print(bool(3)) # True
```
