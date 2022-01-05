
# 파이썬 소스코드
``` python
# 문제점 for i in range(hash, self.size): 에 빈공간이 없다면???
class CloseHash:
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
            self.hash_table[hash] = [key, value]
        else:
            # 가장 가까운 빈 공간 탐색
            for i in range(hash, self.size):
                if self.hash_table[i] == 0 :
                    self.hash_table[i] = [key, value]
                    return
                # 같은 key 발견 -> 교체
                elif self.hash_table[i][0] == key:
                    self.hash_table[i][1] = value
                    return
            print("공간이 부족합니다.")
            return




    def  read_data(self,key):
        hash = self.get_hash(key)

        for i in range(hash, self.size):
            if self.hash_table[i]:
                if self.hash_table[i][0] == key:
                    print(self.hash_table[i][1])
                    return
        print("해시테이블내 요청하신 값은 없습니다.")
        return


    def remove_data(self,key):
        hash = self.get_hash(key)

        for i in range(hash,self.size):
            if self.hash_table[i]:
                if self.hash_table[i][0] == key:
                    self.hash_table[i] = 0
                    print("요청하신 값을 삭제하였습니다.")
                    return

        print("해시테이블내 요청하신 값은 없습니다.")
        return
```
## 테스트 케이스
```python
# Test

h_table = CloseHash(8)

# 1. 같은 해쉬값을 같는지 확인
data1 = 'aa'
data2 = 'ad'
print(ord(data1[0]), ord(data2[0])) #97, 97

# 2.
h_table.save_data('aa', '3333')
h_table.save_data('ad', '9999')
print(h_table.hash_table) # [0, ['aa', '3333'], ['ad', '9999'], 0, 0, 0, 0, 0]

h_table.read_data('ad') # 9999

h_table.remove_data('aa') # 요청하신 값을 삭제하였습니다.
print(h_table.hash_table) # [0, 0, ['ad', '9999'], 0, 0, 0, 0, 0]

h_table.remove_data('ad') # 요청하신 값을 삭제하였습니다.
print(h_table.hash_table) # [0, 0, 0, 0, 0, 0, 0, 0]
```
