[이것과 비교해서 공부](https://github.com/murjune/today_junelog/blob/main/%EC%8A%A4%ED%84%B0%EB%94%94/4.%20HashTable/Open%20Hashing.md)
# 파이썬 소스코드
``` python
import hashlib


class OpenHash:

    def __init__(self,size):

        self.size = size
        self.hash_table = [0 for i in range(self.size)]

    def hash_function(self,key):
        import hashlib
        Hash_object = hashlib.sha256()
        Hash_object.update(key.encode('utf-8'))
        hex_dig = Hash_object.hexdigest()
        Hash = int(hex_dig,16)
        Hash%= self.size
        return Hash

    def save_data(self,key,value):
        hash = self.hash_function(key)

        if not self.hash_table[hash]:
            self.hash_table[hash] = [[key, value]] # 1. 이중 list 으로 변환
        else:
            for i in range(len(self.hash_table[hash])):
                if self.hash_table[hash][i][0] == key: # 2. value값 덮어 쓰기
                    self.hash_table[hash][i][1] = value
                    return
            self.hash_table[hash].append([key, value]) # 3. 추가

    def  read_data(self,key):
        hash = self.hash_function(key)
        if not self.hash_table[hash]:
            print("요청하신 값이 해쉬테이블내에 없습니다.")
        else:
            for i in range(len(self.hash_table[hash])):
                if self.hash_table[hash][i][0] == key:
                    print(self.hash_table[hash][i][1])
                    return
            print("요청하신 값이 해쉬테이블내에 없습니다.")

    def remove_data(self,key):
        hash = self.hash_function(key)
        if not self.hash_table[hash]:
            print("요청하신 값이 해쉬테이블 내에 없습니다.")
        else:
            for i in range(len(self.hash_table[hash])):
                if self.hash_table[hash][i][0] == key:
                    if len(self.hash_table[hash]) == 1: # 길이가 1이면
                        self.hash_table[hash] = 0
                    else:
                        del self.hash_table[hash][i] # i번째 요소 삭제
                    return
            print("요청하신 값이 해쉬테이블 내에 없습니다.")

```
# 테스트 케이스
```python
# Test
h_table = OpenHash(8)
h_table.save_data('aa', '1111')
h_table.save_data('ad', '2222')

# 단순히 아스키 코드를 썼을 때와 다르게 Collison이 일어나지 않았다!!

print(h_table.hash_table) # [0, 0, 0, 0, 0, 0, [['aa', '1111']], [['ad', '2222']]]

h_table.read_data('aa') # 1111
h_table.read_data('ad') # 2222

h_table.remove_data('aa')
print(h_table.hash_table) # [0, 0, 0, 0, 0, 0, 0, [['ad', '2222']]]

h_table.remove_data('Data') # 요청하신 값이 해쉬테이블 내에 없습니다.
print(h_table.hash_table) # [0, 0, 0, 0, 0, 0, 0, [['ad', '2222']]]
```
