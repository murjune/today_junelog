## 2-3: list(자료형)
``` python
#sort - 정렬
a = [1, 2, 4, 8, 0]
a.sort()
print(a) #[0, 1, 2, 4, 8]
```
``` python
#reverse- 순서 바꾸기
a = [1, 2, 4, 8, 0]
a.reverse()
print(a) #[0, 8, 4, 2, 1]
```
``` python
#insert - 특정 인덱스에 삽입, remove
a = [1, 2, 4, 8, 0]
a.insert(0, 3) #0번째에 3삽입
print(a) # [3, 1, 2, 4, 8, 0]

a.remove(0) # 0이라는 값 없애라, 가장먼저 있는 0 지움
print(a) # [3, 1, 2, 4, 8]

```
