
``` python
t1 = ()
t2 = (1,) #t2 = (1,)처럼 단지 1개의 요소만을 가질 때는 뒤에 콤마(,)를 반드시 붙여야 한다
t3 = (1, 2, 3)
t4 = 1, 2, 3 # t4 = 1, 2, 3처럼 괄호( )를 생략해도 무방하다는 점
t5 = ('a', 'b', ('ab', 'cd'))
```
#튜플 append del 불가능
#슬라이싱, 인덱싱, 곱하기 더하기는 된다.
#튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.

1. 리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
2. 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

## 튜플 요솟값을 삭제or 변화를 줄 때

``` python
# 변경 불가능!!

# 빼기 안됨
t1 = (1, 2, 'a', 'b')
del t1[0] # 응 안돼~

# 요소 바꾸기도 안돼!!
t1 = (1, 2, 'a', 'b')
t1[0] = 'c' # 응 안돼

```

## 더하기, 인덱싱, 슬라이싱은 된다.

``` python
# 인덱싱 
t1 = (1, 2, 'a', 'b')
print(t1[0]) # 1
print(t1[3]) # 'b'

# 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[1:]) # (2, 'a', 'b')

# 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2 # (1, 2, 'a', 'b', 3, 4)

# 곱하기
t2 = (3, 4)
print(t2 * 3 ) # (3, 4, 3, 4, 3, 4)

# 튜플 길이
t1 = (1, 2, 'a', 'b')
print(len(t1)) # 4
```

