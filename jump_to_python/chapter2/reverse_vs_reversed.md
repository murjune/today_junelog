## reverse vs reversed ***

#reverse
1. reverse는 list타입에서 제공하는 함수이다.
``` python
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'a': 1, 'b': 2, 'c': 3}
s = 'abc'

l.reverse()  # list의 순서를 뒤집어줌
t.reverse()  # 지원 안함 -> reversed 사용해야하는 것이 좋다
d.reverse()  # 지원 안함 -> reversed 사용해야하는 것이 좋다
s.reverse()  # 지원 안함 -> reversed 사용해야하는 것이 좋다
```
2. reverse는 값을 반환하지 않고, 단순히 해당 list를 뒤섞어준다.
``` python
# replace

a = ['a', 'b', 'c']
a_reverse = a.reverse() # 지정 안됨

print(a_reverse)  # None
print(a)  # ['c', 'b', 'a']
```
#reversed
1. reversed는 내장함수로, list에서 제공하는 함수가 아니다.
``` python
# reversed

a = ['a', 'b', 'c']
print(tuple(reversed(a))) # ('c', 'b', 'a')
print(list(reversed(a))) # {'c', 'a', 'b'}
print(set(reversed(a))) # {'c', 'a', 'b'}

print(str(reversed(a))) #안됨, 아래와 같은 방법을 사용하자
print(''.join(reversed(a))) # cba

# 추가로 딕셔너리는 시퀀셜한 타입이 아니므로 지원하지 않는다.

```
