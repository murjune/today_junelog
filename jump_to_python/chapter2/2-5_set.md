# 집합

## 자료형 바꾸기
``` python
s1 = set([1,2,3]) # {1, 2, 3} # list -> set
print(s1)
s1 = tuple(s1) # (1, 2, 3) # set -> tuple
print(s1)
s1 = list(s1) # [1, 2, 3] # tuple -> listh
print(s1)
```

## set의 (합,교,차)집합
``` python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

#교집합

print(s1 & s2) #{3}
print(s1.intersection(s2))

# 합집합

print(s1 | s2) # {1, 2, 3, 4, 5}, 중복된 건 하나만 표기됨
print(s1.union(s2))

# 차집합

print(s1 - s2) # {1, 2}
print(s1.difference(s2))
```

## set 자료형 함수들
``` python
#더하기(add)

s1 = {1, 2, 3}
s1.add(4)
print(s1) #{1, 2, 3, 4}

#값 여러 개 추가하기(update)

s1 = {1, 2, 3}
s1.update((2, 3, 5, 7)) # 여기서도 물론 중복된 건 추가 안됨
print(s1) # {1, 2, 3, 5, 7}

# 특정 값 제거하기(remove)

s1 = {1, 2, 3}
s1.remove(2) # {1, 3}
print(s1)
s1.remove(4) # KeyError: 4
print(s1)
```
