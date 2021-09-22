
출처: https://blockdmask.tistory.com/531 [개발자 지망생]

# map 함수란?
```
map(function, iterable)

map 함수의 모양은 위와 같다.

첫 번째 매개변수로는 함수가 오고
두 번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)이 옵니다.

map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 혹은 tuple로 형 변환시켜주어야 한다.

함수의 동작은 두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 함수다.



즉, 정리하면 map(적용시킬 함수, 적용할 값들)인 것이다.
```

## 예시
``` python
arr = [1,2,3,4,5]

def add(n): # 리스트 값에 1씩 더해 주는 함수
    return n + 1

result = list(map(add, arr)) # arr에 add함수를 적용

# map반환을 list 로 변환
print(result)
```
