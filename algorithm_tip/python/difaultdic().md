# difaultdic()
참고1: https://dongdongfather.tistory.com/69
참고2: https://www.youtube.com/watch?v=zF01pfp1MOo
difaultdic() 딕셔너리를 만드는 서브클래스이다.
```
difaultdic()와 dict()는 거의 유사하지만
difaultdic() 인자로 주어지는 객체의 기본값을 딕셔너리의 초기값으로 설정할 수 있다.

즉, difaultdic() 말 그대로 처음 key의 값을 주어지지 않으면 해당 key에 대한 값을 default값으로 지정하겠다는 것이다.
이 점이 알고리즘 문제 풀 때  단순 dic()보다 훨씬 유용한 점이다. 
```

## 기본 작동원리

``` python
from collections import  defaultdict
d = defaultdict(str) # 초기값을 str으로 설정

print(d) # defaultdict(<class 'str'>, {})
```
### 예시

1. str
``` python

from collections import  defaultdict


d = defaultdict(str) # 초기값을 str으로 설정
d['1'] = 'a'
d['2']
print(d)
# defaultdict(<class 'str'>, {'1': 'a', '2': ''})
# '2'로 호출만 해도 '2': '' 와 같이key와 value값이 들어간다.
# 즉 초기값 ''

```
2. int
``` python

from collections import  defaultdict

d = defaultdict(int) # 초기값을 str으로 설정
d['1']
print(d)
# defaultdict(<class 'int'>, {'1': 0})
# 초기값 0

```
3. list

``` python
from collections import  defaultdict

d = defaultdict(list) # 초기값을 str으로 설정
d['1']
print(d)
# defaultdict(<class 'list'>, {'1': []})
# 초기값 []


```
