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

예시1) - str
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
## mutable 객체

Mutable
