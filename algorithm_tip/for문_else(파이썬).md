http://pyengine.blogspot.com/2019/12/for-else.html
# 파이썬에는 for문에 특이한 else기능이 하나 더 있다.

이런 문법들을 사용하면, 코드가 훨씬 간결해지고 문제 풀기도 편하다.

for문 속 break문이 빠져나갈 경우의 역 상황을 간결하게 코딩할 수 잇음!!

# 사용법
```
for문을 사용하다보면, 루프 중간에 break 문으로 빠져나오는 경우들이 있는데,
이게 break문이 걸려서 빠져나가는지 아닌지를 판단이 필요한 경우가 있다.

보통은  flag등을 둬서, 처리하는게 기존의 방식이라면,
for문과 같은 레벨에 else를 둬서 break없이 빠져나온 경우를 처리하는 방법이다.

```

## else가 사용되는 경우

``` python
for x in range(4):
  if x == 4:
    print ('loop out')
    break
else:
    print ('loop end')

# 출력값: loop end

    
```

## else가 사용 안되는 경우

``` python
for x in range(4):
  if x == 2:
    print ('loop out')
    break
else:
    print ('loop end')

# 출력값: loop out
```
