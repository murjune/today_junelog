# set과 dict 자료형

set 자료형이나 dict 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다는 특징있다.

## 예시
``` python
a = {1,2,3}
print(a[1])

# 'set' object is not subscriptable
```
그러나  특정한 데이터가 이미 등장한 적이 있는지 여부를 체크할 때 매우 효과적이다.
특정 데이터(원소)가 존재하는지 검사하는 연산의 시간 복잡도가 O(1)이기 떄문이다.

## 예시
``` python

a = {1,2,3}

arr=  [2,3,4,5,9]

for i in arr:
    if i in a:
        print(f"{i}는 arr 속에 있습니다.")

# 출력값

# 2는 arr 속에 있습니다.
# 3는 arr 속에 있습니다.
```
