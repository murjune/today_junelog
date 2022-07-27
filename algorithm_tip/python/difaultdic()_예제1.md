# 예제1: 문자열에 있는 알파벳 갯수를 구해보자.  


풀이 2와 같이 defaltdict() 사용 안하면, key가있는지 검사해야하고, 초깃값을 0 으로 설정해줘야하기 떄문에 번거롭다.
## 풀이1
``` python
# 풀이: defaultdict(int) 사용

from collections import  defaultdict

name = 'king strong JuneWon'
name_d = defaultdict(int)

for i in name:
    name_d[i] +=1 # 키에 값이 없다면 값을 0으로 초기화

print(name_d)
# defaultdict(<class 'int'>, {'k': 1, 'i': 1, 'n': 4, 'g': 2, ' ': 2, 
# 's': 1, 't': 1, 'r': 1, 'o': 2, 'J': 1, 'u': 1, 'e': 1, 'W': 1})

```
## 풀이2
``` python

# defaltdict() 사용 안했을 때 (dict()만을 사용) 

name = 'king strong JuneWon'
name_d = dict()

for i in name:
    if i in name_d: # key값이 있는 지 확인
        name_d[i] +=1
    else:               # 없으면 key의 초깃값 0으로 설정
        name_d[i] = 0

print(name_d)
# {'k': 0, 'i': 0, 'n': 3, 'g': 1, ' ': 1, 's': 0,
# 't': 0, 'r': 0, 'o': 1, 'J': 0, 'u': 0, 'e': 0, 'W': 0}


```

