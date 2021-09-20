참고:https://codechacha.com/ko/python-convert-list-to-string/


# 1. list -> str
``` python
str_list = ['This', 'is', 'a', 'python tutorial']
result = ' '.join(str_list)
print(result) # This is a python tutorial

```
# 숫자가 포합되어 있는 list -> str

## 방법 1
``` python

str_list = [1, 2, 3, 4, 5]
result = ' '.join(str(s) for s in str_list)
print(result) # 1 2 3 4 5

```

## 방법 2: map()으로 숫자를 문자열로 변환

``` python

str_list = [1, 2, 3, 4, 5]
result = ' '.join(map(str, str_list))
print(result) # 1 2 3 4 5

```
