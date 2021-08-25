# for문의 list 내포

## 예시 1
``` python
a = [1,2,3,4,5]
result =[i*3 for i in a if i % 2 == 0]
print(result) # [6, 12]
``` 
위 코드는 다음과 같다.
```python
a = [1,2,3,4,5]
result= []
for i in a:
    if i % 2 == 0:
        result.append(i *3)
print(result) # [6, 12]
```

## 예시 2

``` python
# 구구단 결과

result = [x * y for x in range(2,10) for y in range(1,10)]
print(result)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9,.....,81]
```
