# sorted 함수 응용

## 오름차순, 내림차순

``` python 
arr = [9, 8, 2, 3, 4]

# 오름차순
result = sorted(arr) # result = sorted(arr, reverse =False) 와 같다.
print(result)

# 내림차순
result2 = sorted(arr, reverse= True)
print(result2)
```

## lamda 
내장 함수에서 자주 사용된다.
``` python
arr = [('이준원', 25), ('양재윤', 24), ('이주원', 31)]

def my_key(x):
    return x[1]

print(sorted(arr, key = my_key)) 
# [('양재윤', 24), ('이준원', 25), ('이주원', 31)]

print(sorted(arr, key = lambda x: x[1]))
# [('양재윤', 24), ('이준원', 25), ('이주원', 31)]
```
key 속성을 이용하여 정렬 기준을 명시해 줄 수 있다. 이떄, 정렬 기준을 보통 lamda 함수형태로 넣어 주는 경우가 많다.

``` python 


arr = [('이준원', 25), ('양재윤', 24), ('이주원', 31)]

# 예시: 나이순 정렬하기 (sorted with key )

ans = sorted(arr, key= lambda  x: x[1]) # 두번쨰 원소 x[1]을 기준으로 정렬
print(ans) # [('양재윤', 24), ('이준원', 25), ('이주원', 31)]

# 예시: 나이 역순으로 정렬하기

ans = sorted(arr, key= lambda  x: x[1], reverse= True)
print(ans) # [('이주원', 31), ('이준원', 25), ('양재윤', 24)]

```
