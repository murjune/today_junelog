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

