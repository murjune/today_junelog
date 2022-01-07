[참고 블로그 1](https://www.fun-coding.org/Chapter09-hashtable.html)  
[참고 블로그 2](https://jinyes-tistory.tistory.com/10)  
[참고 블로그 3](https://velog.io/@cyranocoding/Hash-Hashing-Hash-Table%ED%95%B4%EC%8B%9C-%ED%95%B4%EC%8B%B1-%ED%95%B4%EC%8B%9C%ED%85%8C%EC%9D%B4%EB%B8%94-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%9D%98-%EC%9D%B4%ED%95%B4-6ijyonph6o)  
[참고 강의](https://www.youtube.com/watch?v=dKqv1mQotNU)

# 0. 해시 테이블(Hash Table)이란 무엇인가??

- Hash Table은 key/value systeam을 사용하여 data를 정리하는 자료 구조이다.  

- Hash는 각기 다른 프로그래밍 언어에 존재하기 때문에 굳이 만들어줄 필요가 없으나,   
    해시 테이블이 어떻게 작동하는지 알아보기 위해서는 구현이 필연적이기 때문에 간단하게 만들어보자!  
    
- JS: object, Python: Dictionary, Go: Map  


Hash Table에 대해 자세히 알아 보기 전에 array와 어떤 점이 다른지 알아보자!

## Hash Table vs array

- array  

다음과 같이 음식점의 메뉴를 array에 저장한다 하면, 다음과 같을 것이다.

```C
menu = [{name: "coffee", price:"3"}, {name: "burger", price:"5"}, {name: "pizza", price:"15"}];
``` 

만약 손님이 pizza의 가격을 알아 보기 위해서는 처음부터 순서대로 menu를 탐색해야한다(Linear Search)  
그러나, menu의 수가 굉장히 많아진다면, 이는 매우 비효율적이게 된다 -O(N)  



- Hash Table

위의 음식점 메뉴를 Hash Table에 담는다면 다음과 같이 된다.
``` C
menu = {coffee : 10, burger: 5, pizza : 15}
```

위와 같이 손님이 pizza의 가격이 궁금하다면, pizza를 key가 되어 , Hash Table이 가격(value)을 제공해 줄 것이다.  
따라서, array와 달리 Hash Table은 **1step**으로 pizza뿐만 아니라 어느 메뉴의 가격을 알 수 있다.

위의 예시와 같이, Hash Table은 **key값만 안다면, 데이터를 바로 받아 올 수 있기 때문에** array에 비해 매우 빠르다.(constant Search)  

항상 1step인 것은 아니다. 이에 대해서는 뒤쪽 Chater에서 설명하겠습니다.

# 1. Hash Table의 작동 원리

Hash Table이 어떤 경우에 쓰이고, 왜 쓰이는지 예시를 통해 알아 봤다. 

Hash Table이 빠른 이유는 array의 reading이 빠른 이유와 흡사한데  
Hash Table이 어떻게 작동되어서 빠른지를 알아보자!

<p align = "center"><img width = "500" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/630px-Hash_table_3_1_1_0_1_0_0_SP.svg.png"></p>  
출처:(https://en.wikipedia.org/wiki/Hash_table)


위 이미지를 보면, 문자열(John smith) 데이터가 해시 함수를 거쳐 숫자(해시 코드 or 해시)로 변경된다. 변경된 이 값(해시)를 배열(buckets)의 key로 삼아 value를 저장한다.   

따라서 Hash Table은 원하는 데이터를 searching하는 과정에서 array와 같이 선형탐색할 필요없이 **해시 함수를** 거쳐 생성된 **해시 값(해시 테이블의 주소값(idx)이라 생각하면 됨)**으로 데이터를 빠르게 찾을 수 있다.  
```
키(Key): 인풋 데이터  *ex) John Smith, Lisa Smith

값(value): 저장할 데이터 *ex) 521-8976, 521-1234

해시 함수(Hash Function): 'key'를 해시 코드로 변경해주는 함수 
```
 
정리

* 위 이미지에서 문자열 데이터가 hash function을 거쳐 숫자열 데이터(Hash)로 변경된다.
* 이제 Hash를 key삼아서 배열에 값을 저장하는 구조다.  

ex) John Smaith(key) -> 02(Hash) 


해시(Hash): 인풋 데이터를 고정된 길이의 숫자열로 변환한 결과물  *위 이미지에서 00~15가 해시(Hash Table의 index값)다.


즉 문자열로 들어온 인풋 데이터를 해시 함수를 통해 숫자열(Hash)로 변경해주고, 이 숫자(Hash)를 키 값 삼아서 배열(buckets)에 값을 저장하는 구조다.   
(파이썬 해시 함수의 경우 환경마다 아웃풋이 달라서 hashlib의 sha1, sha256을 쓰기도 함)

# 2. 리스트를 활용한 간단한 해시 테이블 구현(feat. Python)

직접 해시 테이블을 구현해보면 모든 작동 원리를 이해하기 쉽다!  
collision이 일어나지 않는다고 가정하고, 정석적인 방식으로 해시 테이블을 구현해보자!

## 0) 해시 테이블 만들기
보통 배열(파이썬 list)로  Hash Table의 크기 만큼 생성 후 에 사용한다. - (메모이제이션 기법)


```python
class HashTable:
    def __init__(self, size):
            self.size = size
            self.table = [0 for i in range(self.size)]
```

## 1)  해시 함수를 통해 key -> Hash로 만들기

1. key -> 숫자형 key (feat. 아스키코드) 
1. 숫자형 key -> idx (= 해시, 해시 테이블의 size로 divide)
      


```python
    def get_hash(self,key):
        key = ord(key)
        idx = key % self.size
        return idx
        
```

## 2) 해시 테이블 값 저장 - O(1)


```python
    def save_data(self,key,value):
        hash = self.get_hash(key)
        self.hash_table[hash] = value
```

## 3) 데이터 읽기 - O(1)


```python
    def read_data(self,key):
        hash = self.get_hash(key)
        if not self.hash_table[hash]:
            print("요청하신 값이 해쉬테이블내에 없습니다.")
        else:
            print(self.hash_table[hash])
```

## 4) 데이터 지우기 - O(1)


```python
       def remove_data(self,key):
        hash = self.get_hash(key)
        if not self.hash_table[hash]:
            print("요청하신 값이 해쉬테이블 내에 없습니다.")
        else:
            self.hash_table[hash] = 0
            print("요청하신 값을 삭제하였습니다.")
```

## 5) 테스트!!

``` python
hash_table = HashTable(8)
hash_table.save_data('a', '111')
hash_table.save_data('b', '222')
hash_table.save_data('c', '333')
hash_table.save_data('d', '444')
print(hash_table.table) # [0, '111', '222', '333', '444', 0, 0, 0]
hash_table.read_data('d') # '444'
hash_table.delete('a') # 요청하신 값을 삭제하였습니다.
print(hash_table.table) # [0, 0, '222', '333', '444', 0, 0, 0] , 지워진것이 확인됨
```

# 3. 해시 충돌(Hash Collision)의 해결(좋은 해시 함수 사용하기)

<img width= '500' src = "https://media.vlpt.us/images/citizenyves/post/743735e6-4a7a-483f-9fe6-5a1ce0b42268/image.png">  
출처 : (https://velog.io/@citizenyves/Hash-table2-hash-colision-%ED%95%B4%EC%8B%9C%EC%B6%A9%EB%8F%8C)

해시 테이블에는 치명적인 문제점이 있다.   
인풋 데이터를 해시 값으로 바꿔주는 과정에서 두 데이터가 다른 key값을 갖음에도 해시 값으로 변환되는 경우가 있다.   
즉, key가 있음에도 들어갈 slot(빈 공간)이 없는 상황을 해시 충돌(Hash Collision)이라고 한다.  

예시를 들자면 다음과 같다.
```
Case 1) size = 10, data의 개수는 11이면 반드시 1개 이상의 데이터가 같은 hash를 같게 된다. (비둘기 집의 원리)  
Case 2) 해시 테이블의 크기가 데이터의 개수보다 크더라도, 위의 그림과 같이 충돌이 발생할 수 있다.
```  

따라서, 해시 테이블을 만들 때, 가장 중요한 점 중 하나가 Collision을 어떻게 하면 극복해낼 수 있을까?이다.  

해시 충돌을 해결하는 대표적인 방법에는 크게 2가지 방법인 Chaining 기법과 Opening Adressing이 있다.  

1. Chaining : 추가적인 공간(메모리)를 활용하여 해결하는 방식
    > - linked- list  
    > - Red-Black Tree  
    
2. Opening Adressing  : 충돌 발생 시 인접한 비어 있는 공간에 저장하는 방식  
    > - 선형 탐색(Linear Probing): 고정폭(보통 +1 or +n)으로 이동하여 빈 공간을 찾음   
    > - 제곱 탐색(Quadratic Probing): 충돌이 일어난 Hash의 제곱값으로 이동하며 빈 공간을 찾음  
    > - 이중 해시(Double Hashing): 충돌이 일어난 Hash에 또 다른 해시 함수를 사용하여 빈 공간을 찾는다.


## 1) 오픈 해싱(Open Hashing)

<img width = "500" src= "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcfHBtM%2FbtqBJeog1Zy%2FvhNFhrlsvpNwwJFeGxX1ok%2Fimg.png">  
출처:(https://en.wikipedia.org/wiki/Hash_table)

오픈 해싱은 해시 테이블의 충돌 문제를 해결하는 대표적인 방법중 하나로 체이닝(Separate Chaining) 기법이라고도 한다. 만약 해시 값이 중복되는 경우, 위의 그림과 같이 먼저 저장된 데이터에 링크드 리스트를 이용하여 중복 해시  데이터를 연결한다.

 
1. linked list를 사용하는 방법
파이썬에는 굳이 링크드 리스트를 안 쓰고 슬롯을 이중 리스트 구조로 활용해서 간단하게 구현할 수 있다.  

[오픈 해싱 파이썬 소스코드 보기(feat. linked list)](https://github.com/murjune/today_junelog/blob/main/%EC%8A%A4%ED%84%B0%EB%94%94/4.%20HashTable/Open%20Hashing.md)    

2. BST의 일종인 Red-Black Tree를 사용하는 방법  

    Java의 jdk7 까지는 linked-list를 사용한 Chaining기법을 활용하여 해쉬 충돌 해결  
    Javadml jdk7에서는 linked-list와 Red-Black Tree를 혼용하여 Chaining기법을 활용하여 해쉬 충돌 해결

    1) 충돌을 한 key-value 쌍의 수가 적을 때는 linked-list  
    2) 임의의 인덱스에 대해서 충돌한 key-value 쌍의 수가 특정 임계치를 넘어가게 되면 linked-list를 RBT로 바꿔서  
    key-value 데이터들을 저장하게 된다.  

    RBT는 일종의 BST중 하나로 탐색,추가,삭제 모두 O(logN)의 시간복잡도를 갖게 된다.(O(N)보다 바교적 훨씬 빠르다)



# Chaining 장단점

장점 :
1) 한정된 저장소(Bucket)을 효율적으로 사용할 수 있다.  
2) 해시 함수(Hash Function)을 선택하는 중요성이 상대적으로 적다.  
3) 상대적으로 적은 메모리를 사용한다. (미리 공간을 잡아 놓을 필요가 없다.)

단점 :
1) 한 Hash에 자료들이 계속 연결된다면(쏠림 현상) 검색 효율을 낮출 수 있다.  
2) 외부 저장 공간을 사용한다.(추가 메모리가 필요)  
3) 외부 저장 공간 작업을 추가로 해야 한다.  

## 2) Open Addressing

<img width= "500" src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FUA8G0%2FbtqBGrh2EYa%2FHEqlOWRt4wQiLsPWK5hoV1%2Fimg.png">  
출처:(https://en.wikipedia.org/wiki/Hash_table)

Open Addressing은 해시 테이블의 충돌 문제를 해결하는 방법 중 가장 대표적인 하나로 Linear Probing으로 설명해보자~

 

구조는 간단하다. 위 그림에서 John Smith와 Sandra Dee의 해시는 똑같이 873이다. 이때 먼저 들어온 John이 873이라는 해시로 공간에 들어 갔으니, 다음으로 들어온 Sandra는 바로 다음 key값(+1)인 874를 키 값으로 가진다.   
해시 중복이 발생하면 해당 해시 값부터 **순차적으로 빈 공간을 찾기 시작한다**. 가장 처음 찾는 빈 공간에 키와 밸류를 저장한다. 

Open Addressing은 저장 효율을 높이는 방법이다.  

[Open Addressing 파이썬 소스코드 보기](https://github.com/murjune/today_junelog/blob/main/%EC%8A%A4%ED%84%B0%EB%94%94/4.%20HashTable/Close%20hashing.md)

## Open Addressing의 장단점
장점 :
1) 또 다른 **추가 저장공간 없이** 해시테이블 내에서 데이터 저장 및 처리가 가능하다.  
2) 또 다른 저장공간에서의 추가적인 작업이 없다.  

단점 :
1) **해시 함수(Hash Function)**의 성능에 전체 해시테이블의 성능이 좌지우지된다.  
2) 데이터의 길이가 늘어나면 그에 해당하는 저장소를 마련해 두어야 한다.

##  추가 1) Python Dictionary 

파이썬의 자료형 중 해시 테이블로 구현된 자료형은 딕셔너리이다.  
파이썬은 내부적으로 Open Addressing 방식을 활용하여 해시충돌을 해결한다.  

이때, 위에서 서술한 것처럼 Open Addressing을 활용할 때, 빈공간이 없을 경우 문제가 발생할 수 있다.  
따라서, 파이썬에서는 **Load Factor**를 작게 설정하여 성능 저하 문제를 해결한다.  

## 추가 2) Load Factor 란?
<img width = "400" src= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvVF-24us_7okImpLhOM74V7BU5bXrzhzjnw&usqp=CAU">  

Load factor는 해시 테이블의 공간이 얼마나 가득 찼는지 측정하는 지표이다.  
> LF = (해시 테이블에 입력된 키의 개수 / 해시 테이블의 전체 인덱스(해시) 갯수)  

LF가 임계치에 도달하면 해시 테이블 크기조정여부, 해시 함수 재작성여부가 결정된다.(보통 임계치: 0.75)  
LF를 낮추면 해시테이블의 성능은 올라간다.
```
Load Factor 예시

# 로드팩터가 0.75에 도달하면 기존 용량을 2배 증가하도록 설정한다.

1. 해시테이블의 초기용량이 10이라고 가정할 때, 10∗0.75=7.5
2. 즉, 7번째 키값을 저장한 후에 용량이 2배로 늘어난다.
3. 결과적으로 기존 용량(10)에서 증가된 용량(20)이 된다.
4. 용량이 증가될 때, 기존 데이터들을 해시함수에 다시 넣어 해시테이블을 재정렬한다.
```



# 4. Hash Table Data Structure의 단점
1. 순서가 있는 배열에는 어울리지 않는다.:  

 상하관계가 있거나, 순서가 중요한 데이터의 경우 Hash Table은 어울리지 않다.  
 순서와 상관없이 key만을 가지고 hash를 찾아 저장하기 때문이다.  
 
 
1. 공간 효율성이 떨어진다.:  

    데이터가 저장되기 전에 미리 저장공간을 확보해 놓아야 한다.   
공간이 부족하거나 아예 채워지지 않은 경우가 생길 가능성이 있다.  


1. Hash Function의 의존도가 높다.:  

    평균 데이터 처리의 시간복잡도는 O(1)이지만, 이는 해시 함수의 연산을 고려하지 않는 결과이다.  
해시함수가 매우 복잡하다면 해시테이블의 모든 연산의 시간 효율성은 증가할 것이다.  

그러나, 해시 테이블은 키를 가지고 빠르게 value에 접근하고 조작할 수 있는 장점이 있어서 많이 사용된다. 예를 들어 주소록 저장형태의 경우 이름 — 전화번호의 매칭을 이용하여 데이터를 처리한다.

# 5. 해시함수

위에 챕터들에서 서술한 것처럼, Hash Table에서는 Collision이 빈번하게 일어나고, 이를 해결하는 것이 매우 중요한 것을 알았다.  
따라서, Collision을 사전에 차단하는 방법이 크게 2가지 방법이 있는데 첫번째는 위에 Load Factor를 활용하여 HashTable의 크기를 조정하는 것이고,   
두번째는 **좋은 해시 함수**를 쓰는 것이다!  

우리가 위에서 사용한 해시 함수는 단순히 Hash Table의 크기로 나눠준 초간단한 해시함수였다.


```python
def hashfucntion(self,key):
        key = ord(key) # key -> 아스키코드
        idx = key % self.size # 해시 테이블의 크기로 나눠주기
        return idx
```

위에 코드에서 key를 아스키코드로 변환해주지 않고, 파이썬 내장 hash()함수를 사용할 수도 있다.


```python
def hashfucntion(self,key):
        key = hash(key) 
        idx = key % self.size # 해시 테이블의 크기로 나눠주기
        return idx
```

그러나, 파이썬의 hash() 함수는 실행될 때마다 값이 달라질 수 있기 때문에 항상 일관된 값을 갖지 않는다.

이 점은 파이썬에는 SHA(Sucure Hash Algorithm, 안전한 해시 알고리즘)이라는 유명한 해시 함수로 해결 가능하다.  
   > 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해시 함수로 유용하게 사용가능하다.  
    

## 예제)SHA-256를 활용한 해싱 


```python
# 1. 문자열 해싱을 위해서는 hashlib 모듈을 사용해야 한다.
import hashlib

# 2. 해시 알고리즘 중 하나인 sha256 방식으로 해싱
Hash_object = hashlib.sha256()

# 3. hashlib.sha256()에 의해 생성된 객체 Hash_object가 update 함수를 호출하면서 문자열이 해싱된다.
Hash_object.update(b"Hello World")

# 4. hexdigest 함수를 사용하여 해싱된 문자열을 얻을 수 있다.
hex_dig = Hash_object.hexdigest()

# 5. 16 진수로 해시값 리턴
print(hex_dig)
# 6. 정수형 반환
print(int(hex_dig,16))
```

    a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
    74888964247292943290829644364954473609342749251111522634754282069725240300654


[SHA 해시 알고리즘을 이용한 해시 함수 + Chaining 기법을 활용한 HashTable 파이썬 소스코드](https://github.com/murjune/today_junelog/blob/main/%EC%8A%A4%ED%84%B0%EB%94%94/4.%20HashTable/SHA256+Chaining.md)
