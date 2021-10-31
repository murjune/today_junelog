# 얇은 복사(Shallow copy)와 깊은 복사(Deep Copy)
```
얕은 복사: 객체를 새로운 객체로 복사하지만, 원본 객체의 주소값을 복사하는 것  
깊은 복사: 전체 복사로, 참조값의 복사가 아닌 참조된 객체 자체를 복사하는 것  
```
앞 장의 list들은 모두 얄은 복사를 통해 주소값만 복사하였다.  
이 떄, list의 Mutable한 특성 때문에 원본 객체의 값 또한 바뀐 것을 확인했다.  

그러나, 알고리즘을 풀 때, 원본 배열을 보존할 필요가 있을 경우가 많기 떄문에  
이럴 때는 깊은 복사를 해야 한다.

# 얕은 복사(Shallow copy)

## 1. list의 슬라이싱

list의 슬라이싱을 통해 tmp에 새로운 값을 할당하였다.  
아래의 결과와 같이 슬라이싱을 통해 값을 할당하여 새로운 주소값(id)를 부여하여, 서로 영향을 받지 않는다.
``` python
# 리스트 슬라이싱
a = [1,2,3,4]

tmp = a[:]

print(a,tmp) # [1, 2, 3, 4] [1, 2, 3, 4]
print(a is tmp) # False

# 원소값을 바꿀 경우

a = [1,2,3,4]

tmp = a[:]
tmp[0] = 0

print(a,tmp) # [1, 2, 3, 4] [0, 2, 3, 4]
print(a is tmp) # False
```

## 2. copy() 메소드
``` python
# Shallow copy - copy() 메소드

a = [1,2,3,4]
tmp = a.copy()

print(a,tmp) # [1, 2, 3, 4] [1, 2, 3, 4]
print (a is tmp) # False - 다른 주소값


```
# 그러나!! 주의!!  

슬라이싱과 copy() 메소드 같은 얕은 복사를 사용할 떄 주의해야할 점이 있다.  

리스트안에 리스트가 들어가 있는 이중 리스트의 경우  
즉, mutable한 객체 안에 mutable한 객체가 들어가 있는 경우에는 문제가 된다...  



아래와 같이 id(a) 와 id(b)의 값은 다르지만  
그 내부의 객체 id(a[0])과 id[b[0]]의 값은 같다.  


``` python
# 예시 1
# 리스트 슬라이싱 - list 속 list안의 원소값에 변화를 주는 경우
a = [[1],[2],[3],[4]]


tmp = a[:]
print( a is tmp) # False 

for i, j in zip(a, tmp):
    print(i is j , end= ' ') # True True True True - list 속 list안의 내용은 원본 배열의 주소값과 같다.

```

재할당을 하는 경우는 문제가 없다. 메모리 주소도 변경

``` python
# 예시 2
# 리스트 슬라이싱 - 2중 리스트 속을 재할당하는 경우
a = [[1,2],[2,3],[3,4],[4,5]]
tmp = a[:]

tmp[0] = [10000]

print(a,tmp) # [[1, 2], [2, 3], [3, 4], [4, 5]] [[10000], [2, 3], [3, 4], [4, 5]]
print(a[0] is tmp[0]) # False - 재할당 되어 각각 다른 주소값을 참조한다.
print(a[1] is tmp[1]) # True

```

하지만, a[0]울 변경하면 tmp[0]도 변경
``` python
# 예제 3
# 리스트 슬라이싱 - 2중 리스트 속의 값을 변경하는 경우 (재할당 X)
a = [[1,2],[2,3],[3,4],[4,5]]
tmp = a[:]

tmp[0].append(100)

print(a,tmp) # [[1, 2, 100], [2, 3], [3, 4], [4, 5]] [[1, 2, 100], [2, 3], [3, 4], [4, 5]]
print (a is tmp) # False - 다른 주소값
print(a[0] is tmp[0]) # True - 같은 주소값
print(a[1] is tmp[1]) # True - 같은 주소값

```

따라서, 원본 이중 list 배열을  유지하기 위해서는 deep copy가 반드시 필요하다.

# 깊은 복사(deep copy)

깊은 복사는 내부에 객체들까지 모두 새롭게 copy !!  

copy.deepcopy 메소드 사용
``` python

# deep copy - copy 모듈 사용

import copy

a = [[1,2],[2,3],[3,4],[4,5]]
tmp = copy.deepcopy(a)

tmp[0].append(100)

print(a,tmp) # [[1, 2], [2, 3], [3, 4], [4, 5]] [[1, 2, 100], [2, 3], [3, 4], [4, 5]]
print (a is tmp) # False - 다른 주소값
print(a[0] is tmp[0]) # False - 다른 주소값
print(a[1] is tmp[1]) # False - 다른 주소값

```
