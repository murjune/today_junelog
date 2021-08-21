연습 문제: https://wikidocs.net/42526

# 2장 연습문제

``` python
# 1
score = [80, 75, 55]

answer = (score[0] + score[1] + score[2]) / 3
print(answer)
```

``` python
# 2
# n이 홀수 인지 짝수 인지 판별하는 프로그램

n = int(input())

if n % 2 == 0:
    print("짝수")
else:
    print("홀수")
```

``` python
# 3

# 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자

jumin = "881120-1068234"
print("연월일: " + jumin[:6])
print("뒷 번호: "+ jumin[7:])
```

``` python
# 4
# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다.
# 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
pin = "881120-1068234"
print(pin[7:8]) # 1
print(pin[7]) # 1
```


``` python
# 5
#다음과 같은 문자열 a:b:c:d가 있다.
#문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

a = "a:b:c:d"

print(a.replace(":", "#"))
```

``` python
# 6

#[1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.

# reverse 사용
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# reversed 사용
a = [1, 3, 5, 4, 2]
a.sort()
print(list(reversed(a)))
```

``` python
# 7
# ['Life', 'is', 'too', 'short'] 리스트를
# Life is too short 문자열로 만들어 출력해 보자.

# 방법1
a = ['Life','is','too','short']

a = ",".join(a)
print(a.replace(",", " "))
# 방법2
a = ['Life','is','too','short']

print(" ".join(a))
```



