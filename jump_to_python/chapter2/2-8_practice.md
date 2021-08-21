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

``` python
# 8
#(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.

a = (1, 2, 3)
b = (4, ) # , 반드시 붙여야 한다.

print(a+ b)
```

``` python
# 9

a = dict()
print(a)

a['name'] = 'python'
print(a) # {'name': 'python'}

a[('a',)] = 'python'
print(a) # {'name': 'python', ('a',): 'python'}

a[[1]] = 'python' # 키에는 list가 들어갈 수 없다.

a[250] = 'python' # {'name': 'python', ('a',): 'python'}
print(a)
```

``` python
# 10
# 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.

a = {'A': 90, 'B': 80, 'C': 70}

print(a['B'])
print(a.get('B', 2)) # 80
print(a.pop('B')) # 80
print(a) # {'A': 90, 'C': 70}
```

``` python
# 11
# a 리스트에서 중복 숫자를 제거해 보자.

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

a = set(a)
print(a)
```


``` python
# 12
#파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
# 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까?
# 그리고 이런 결과가 오는 이유에 대해 설명해 보자.

a = b = [1, 2, 3]
a[1] = 4 # a = b = [1, 4, 3]
print(b)
# a와 b 변수는 모두 동일한 [1, 2, 3]이라는 리스트 객체를 가리키고 있기 때문이다.
```


