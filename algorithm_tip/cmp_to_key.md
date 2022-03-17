[참고 문헌 ]: https://wikidocs.net/109303
---

# cmp_to_key

`functools.cmp_to_key(func)` 함수는 sorted와 같은 정렬 함수의 key 매개변수에 함수(func)를 전달할 때 사용하는 함수이다.  
단, func 함수는 두 개의 인수를 받아들이고, 첫번째 인수를 기준으로 그들을 비교하여, 작으면 음수, 같으면 0, 크면 양수를 반환하는 비교 함수이어야 한다.  
(e. func(a,b), if (a>b) : 1 elif(a==b) : 0 else: -1 )

# 예제  
2차원 평면 위의 점 N개가 다음과 같이 (x, y) 좌표의 리스트로 주어진다.  
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

- [input] : [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]. 
- [output] : [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]. 
```python

from functools import *

arr =[(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]

def comparator(a,b):
    if (a[1] > b[1]): return 1
    elif ( a[1] < b[1]) : return -1

    elif (a[1] == b[1]):
        if (a[0] > b[0] ) : return 1
        elif (a[0] == b[0]) : return 0
        else : return -1

arr = sorted(arr, key = cmp_to_key(comparator))
print(arr) #[(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]

# 동일
arr2 = sorted(arr, key = lambda x : (x[1],x[0]))
print(arr2) # #[(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)]
```

