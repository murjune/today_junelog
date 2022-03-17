# __str__  메서드

Object클래스의 멤버메서드인 __str__메서드는 자바의 toString() 메서드와 동일한 역할을 한다.  
```pyhton
class Myname:
    def __init__(self,name):
        self.name = name



n = Myname("머준원")
print(n) # <__main__.Myname object at 0x7fc330061130> 출력
```
이번에는 __str__메서드를 오버라이딩해보자
```python
class Myname:
    def __init__(self,name):
        self.name = name
    
    # 오버라이딩
    def __str__(self):
        return "{0}".format(self.name)


n = Myname("머준원")
print(n) # 머준원

```
# __repr__ vs __str__
__str__이 서로 다른 자료형 간 인터페이스를 제공하기 위한 목적으로 존재한다면, __repr__는 해당 객체를 인간이 이해할 수 있는 표현으로 나타내기 위한 용도이다.

[출처: https://it-neicebee.tistory.com/104 [IT's Portfolio]
