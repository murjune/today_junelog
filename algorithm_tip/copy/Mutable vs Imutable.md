참고: https://velog.io/@aonee/Python-%EC%9E%90%EB%A3%8C%ED%98%95%EC%9D%98-%EA%B0%92-%EC%A0%80%EC%9E%A5-%EB%B3%B5%EC%82%AC-copy  
참고: https://crackerjacks.tistory.com/14


# 파이썬의 복사
```
알고리즘 문제를 풀 때, 원본 배열을 유지하면서 그 값을 복사할 일이 종종 쓰인다.
ex) dfs 문제 풀때, 2중 list 그래프를 복사할 경우

나는 이떄 주로 [:](슬라이싱)을 이용하였는데, 문제를 풀때 이중 list를 복사할 경우
원본 배열의 데이터 또한 변경되어서 골치 아팠다. 

따라서, 이를 해결하기 위해 깊은 복사와 얕은 복사에 대해 공부하도록 하겠다!!

-> 객체를 무작정 복사해서 사용하면 원본 객체가 핸들링되어 데이터가 변경되어서 큰 문제를 야기할 수 있기 때문에 
   객체를 복사할 때에는 주의해서 다뤄야 한다.
```

# 자료형의 값 저장

## Immutable 객체

파이썬에서 변수의 선언을 보면
``` python
a = 1
```
  
파이썬에서는 a와 1은 별개의 존재이다.  
a라는 변수는 integer 1이라는 객체를 뜻할 뿐, a 변수가 정수 1의 값과 동일하다는 것이 아니다.  

cf) c언어에서의 변수 선언
``` c
int a = 1;
# Integer 자료형 변수 a는 1의 값을 가지며 변수 a와 1은 같은 존재
```

예시 1) - str(Immutable)
``` python
a = 1
tmp = a
print(a, tmp) # 1 1
print(id(a),id(tmp)) # 1368402848048 1368402848048 (같은 주소값)
print(a is tmp) # True
```

위 코드에서 a,b는 같은 값(1)을 같는다.  
이때, b의 값에 변화를 준다면?
``` python
a = 1
tmp = a
tmp = 2
print(a,tmp) # 1 2
print(id(a),id(tmp)) # 2107240245552 2107240245584 (다른 주소값)
print(a is tmp) # False
```
위와 같은 결과가 나오는 이유는, int의 자료형이 immutable한 특징을 가졌기 때문이다.  
immutable한 객체는 생성된 후 수정이 불가능 하다.  

-> Immutable한 객체는 반복 가능한 객체일 경우다.

## 주의

재할당하는 것은 애초에 변수를 다시 할당하는 것이기 때문에, mutable과 immutable과는 다른 문제이다.
``` python
s = 'abc'
# s[0] = 'b' # 'str' object does not support item assignment
print(s) # abc
print(id(s)) # 140301282108208

s = 'hi bro'
print(s) # hi bro
print(id(s)) # 140301282193904 - 변수 재할당 하였기 때문에 주소값이 바뀜

```
## mutable 객체

Mutable한 객체에는 대표적으로 list가 있다.  
``` python

a = [1,2,3,4]
tmp = a
print(id(a), id(tmp)) # 140516163695552 140516163695552
print(a is tmp) # True
print(a,tmp) # [1, 2, 3, 4] [1, 2, 3, 4]
```
위의 방식대로 tmp의 값을 바꾼다면

예시 2) - list(mutable)
``` python

a = [1,2,3,4]
tmp = a

tmp[1] = 0
print(id(a), id(tmp)) # 140389864813504 140389864813504 (같은 주소값)
print(a is tmp) # True
print(a,tmp) # [1, 0, 3, 4] [1, 0, 3, 4]

```
Immutable한 str의 결과와 다르게 tmp의 원소값을 바꾸어 주었을 때, a의 값 또한 바뀌었다.  
이는 list가 mutable한 특징을 가졌기 때문이다.  

자세히 설명하자면, a와 tmp는 같은 주소값을 참조한다는 것을 의미한다.  
그런데 list는 mutable하기 때문에 tmp값이 바뀌어 버리면 그 주소에 있는 값 또한 바뀌기 때문에  
같은 주소값을 참조하는 a 또한 값이 바뀌는 것이다.  

예시 3) - list와 str 정리
``` python
# str
a = 1
tmp = a

print(a is tmp) # True - 각각 동일한 레퍼런스(주소값)를 참조하고 있다.

tmp = 0
print(a is tmp) # False - int형 변수는 Immutable 하므로 값이 바뀔 수 없어 다른 id 값을 갖음

# list
b = [1, 2, 3, 4]
tmp2 = b
print(b is tmp2) # True - 각각 동일한 레퍼런스(주소값)를 참조하고 있다.

tmp2[1] = 0
print(b is tmp2) # True - list형 변수는 Mutable하므로 값만 바뀌고 여전히 같은 주소값을 참조한다. 
                                        # 때문에 tmp2의 값을 바꿔도 b의 값이 따라서 바뀌는 것이다.

```
![image](https://user-images.githubusercontent.com/87055456/139575575-d32c9b1d-3a79-42de-bd7a-a282da7281cc.png)
