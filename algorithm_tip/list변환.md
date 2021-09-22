참고:https://codechacha.com/ko/python-convert-list-to-string/

# join 함수
join은 문자열,list,tuple형 모두 합칠 수 있다.
## ''.join(리스트)
```


'구분자'.join(리스트)

join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수다.

1) ''.join(리스트)
''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것이다.

2) '구분자'.join(리스트)
'구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐준다.
'_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 준다.

''.join(리스트)는 '구분자'.join(리스트)에서 '구분자'가 그냥 공백인 것과 같다.

즉, 정리하자면 join함수의 진짜 모양은 '구분자'.join(리스트)이다.



출처: https://blockdmask.tistory.com/468 [개발자 지망생]


```

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
