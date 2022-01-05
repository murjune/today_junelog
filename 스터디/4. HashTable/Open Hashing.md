
# Python 소스코드
``` python

class OpenHash:
    def __init__(self,size):
        self.size = size
        self.hash_table = [0 for i in range(self.size)]

    def get_hash(self,key):
        key = ord(key[0])
        idx = key % self.size
        return idx

    def save_data(self,key,value):
        hash = self.get_hash(key)

        if not self.hash_table[hash]:
            self.hash_table[hash] = [[key, value]] # 1. 이중 list 으로 변환
        else:
            for i in range(len(self.hash_table[hash])):
                if self.hash_table[hash][i][0] == key: # 2. value값 덮어 쓰기
                    self.hash_table[hash][i][1] = value
                    return
            self.hash_table[hash].append([key, value]) # 3. 추가

    def  read_data(self,key):
        hash = self.get_hash(key)
        if not self.hash_table[hash]:
            print("요청하신 값이 해쉬테이블내에 없습니다.")
        else:
            for i in range(len(self.hash_table[hash])):
                if self.hash_table[hash][i][0] == key:
                    print(self.hash_table[hash][i][1])
                    return
            print("요청하신 값이 해쉬테이블내에 없습니다.")

    def remove_data(self,key):
        hash = self.get_hash(key)
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
## 테스트 케이스
``` python
# Test

h_table = OpenHash(8)


h_table.save_data('aa', '1111')
h_table.read_data('aa') # 1111

# 같은 해쉬 값 같는 data들  검사
data1 = 'aa'
data2 = 'ad'

print(ord(data1[0])) # 97
print(ord(data2[0])) # 97

#   똑같은 Hash값을 갖는 'ad, 22' 저장
h_table.save_data('ad', '2222')
print(h_table.hash_table) # [0, [['aa', '1111'], ['ad', '2222']], 0, 0, 0, 0, 0, 0]

h_table.read_data('aa') # 1111
h_table.read_data('ad') # 2222

h_table.remove_data('aa') # [0, [['ad', '2222']], 0, 0, 0, 0, 0, 0]
print(h_table.hash_table)
h_table.remove_data('Data') # 요청하신 값이 해쉬테이블 내에 없습니다.
h_table.remove_data('ad')
print(h_table.hash_table) # [0, 0, 0, 0, 0, 0, 0, 0]
```
