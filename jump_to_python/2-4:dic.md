# 딕셔너리

딕셔너리: 엄청 중요, 순서가 없음
key와 value로 이루어져있다.

``` python
dic = {Key1:Value1, Key2:Value2, Key3:Value3}
a = { 'a': [1,2,3]} # Value에 리스트도 넣을 수 있다.
```
1) key(입력), value(출력)
``` python
dic = {1: '이준원'} # key: 1, value: '이준원'
print(dic[1]) # 이준원
print(dic[0]) #key가 없기 때문에 오류
```

2) 딕셔너리 쌍 추가, 삭제하기


``` python
#딕셔너리 쌍 추가

a = {1: 'a'}
a[2] = 'b'
print(a) #{1: 'a', 2: 'b'}
```
{1: 'a'} 딕셔너리에 a[2] = 'b'와 같이 입력하면 딕셔너리 a에 Key와 Value가 각각 2와 'b'인 2 : 'b'라는 딕셔너리 쌍이 추가된다.

``` python
a = {1: 'a', 2: 'b'}
a['name'] = 'pey'
print(a) #{1: 'a', 2: 'b', 'name': 'pey'}
```
딕셔너리 a에 'name': 'pey'라는 쌍이 추가되었다.

```
a = {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1,2,3]
print(a) # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
```
Key는 3, Value는 [1, 2, 3]을 가지는 한 쌍이 또 추가되었다.
``` python
#딕셔너리 요소 삭제하기
del a[1]
print(a) # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}
```
위 예제는 딕셔너리 요소를 지우는 방법을 보여 준다. 
del 함수를 사용해서 del a[key]처럼 입력하면 지정한 Key에 해당하는 {key : value} 쌍이 삭제된다.

3) 주의할 점
``` python
a = {1: 'a', 1:'b'}
print(a) # {1: 'b'} key가 중복되면 안됨, key가 핵심이다.
```
딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점을 주의해야 한다. 다음 예에서 볼 수 있듯이 동일한 Key가 2개 존재할 경우 1:'a' 쌍이 무시된다.
``` python
a = {[1,2] : 'hi'}
#Traceback (most recent call last): File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'list'
```
또 한 가지 주의해야 할 사항은 Key에 리스트는 쓸 수 없다.
단 Value에는 변하는 값이든 변하지 않는 값이든 상관없이 아무 값이나 넣을 수 있다.

4) 딕셔너리 관련 함수들
```
#Key, value 리스트 만들기(keys, values, items)

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

print(a.keys()) # dict_keys(['name', 'phone', 'birth'])

print(a.values())  # dict_values(['pey', '0119993323', '1118'])

print(a.items()) # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

print( list(a.keys()) ) # ['name', 'phone', 'birth'] # list 변환
```

``` python

# clear

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a.clear()
print(a) # {}

#get

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a['name']) # pey
print(a.get('name')) # pey

#거의 같지만, 없는 거 찾을 때 유리
print(a.get(4)) # none
print(a.get('name', 3) # pey

# in: dic안에 key가 있는지 찾아볼 때 쓰는 함수

print('name' in a) # True
print('email' in a) # False
```

5) 활용: dic 반복문 사용

``` python
dic_a = {1: '이준원', 2: '이주원', 3: '장선혁'}

for k, v in dic_a.items():
    print("사물함 키는:{0}".format(k))
    print("사물함 주인은:{0}".format(v))

#사물함 키는:1
#사물함 주인은:이준원
#사물함 키는:2
#사물함 주인은:이주원
#사물함 키는:3
#사물함 주인은:장선혁
```

