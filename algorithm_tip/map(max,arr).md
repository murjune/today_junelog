#  arr(ex.2차원 배열)에서 max값만 추출하는 파이썬 코드

``` python

# 이차원 배열에서의 max
arr = [[1,2,3], [2,3,4]]

print(max(map(max,arr))) # 4

print(list(map(max, arr))) # [3, 4]
```
