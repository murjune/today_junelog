# Counter

``` python
# 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공한다.
# list와 같은 반복가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장 했는지를 알려준다.

from collections import Counter

arr = ['a', 'a', 'c', 'e', 'd', 'b']
counter = Counter(arr)

print(counter['a']) # 2
print(counter['b']) # 1
print(dict(counter)) # {'a': 2, 'c': 1, 'e': 1, 'd': 1, 'b': 1}

```
