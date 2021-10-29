
참고: https://blockdmask.tistory.com/531 [개발자 지망생]  
참고2 : https://dojang.io/mod/page/view.php?id=2286 - 이걸 집중적으로 봐야함!

# map 함수란? -  리스트의 요소를 지정된 함수로 처리해주는 함수
```
map(function, iterable)

map 함수의 모양은 위와 같다.

첫 번째 매개변수로는 함수가 오고
두 번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)이 옵니다.

map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 혹은 tuple로 형 변환시켜주어야 한다.

함수의 동작은 두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 함수다.



즉, 정리하면 map(적용시킬 함수, 적용할 값들)인 것이다.
```

# 예시 1
``` python
arr = [1,2,3,4,5]

def add(n): # 리스트 값에 1씩 더해 주는 함수
    return n + 1

result = list(map(add, arr)) # arr에 add함수를 적용

# map반환을 list 로 변환
print(result)
```


# 예시 2

## for문 을 통해 모든 원소 int형으로

``` python

a = [1.2, 2.5, 3.7, 4.6]

for i in range(len(a)):
    a[i] = int(a[i])
print(a) # [1, 2, 3, 4]
```


## map을 사용
 map에 int와 리스트를 넣으면 리스트의 모든 요소를 int를 사용해서 변환합니다. 그다음에 list를 사용해서 map의 결과를 다시 리스트로 만들어줍니다.
``` python
a = [1.2, 2.5, 3.7, 4.6]

print(list(map(int,a))) # [1, 2, 3, 4]

```
map에는 리스트뿐만 아니라 모든 반복 가능한 객체를 넣을 수 있습니다
ex) 리스트, 문자열, 딕셔너리, 세트
![image](https://user-images.githubusercontent.com/87055456/139444158-27f1d21c-a92b-441e-8090-1cb79ba288f8.png)

