# chapter3 연습문제

## 1 
``` python
# 1번
# 다음 코드의 결과 값은 ? shirt

a = "Life is too short, you need python"

if "wife" in a:  # 거짓
    print("wife")
elif "python" in a and "you" not in a: # 거짓
    print("python")
elif "shirt" not in a: # 참 , 출력!
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")
```

## 2
``` python
# 2번
# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

a = 1
answer = 0
while True:
    answer += a*3
    a +=1
    if a*3 > 1000:
        break
print(answer) # 166833

```

## 3
``` python
# 3
# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자

i =1
while i <6:
    print("*"*i)
    i +=1
```

## 4
``` python
# 4
# for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

for i in range(1,101):
    print(i)
```

## 5
``` python
# 5
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for 문을 사용하여 A 학급의 평균 점수를 구해 보자

a_score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum_score = 0

for i in a_score:
    sum_score += i

average_score = sum_score / (len(a_score))

print(average_score)

```

## 6
``` python
# 6
# 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
# 리스트 내포를 사용해서 표현해보자
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result) # [2, 6, 10]
# 답
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 ==1]
print(result) # [2, 6, 10]

```

