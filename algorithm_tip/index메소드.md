# index 메소드 사용법

arr 속에 x라는 원소의 위치를 찾기 위해 사용할 수 있는 메소드이다.

## 예시 1
``` python
arr = [1,2,3,4,5]
x = 2

print(arr.index(x))
print(arr.index(6)) # ValueError: 6 is not in list
 
```

## 예시 2

``` python
arr = [1,2,3,4,5]
x = 6

if x in arr:
  print(x)
else:
  print("x값이 arr 내에 존재 하지 않습니다.")
  



```
