# for문 범위설정

``` python

a ='abcdefg'

# len(a) =7

for i in range(0, len(a), 2):  # 간격 2
    print(a[i], end=' ') # a c e g (i= 0 2 4 6)

for i in range(0, len(a), 3): # 간격 3
    print(a[i], end=' ') # a d g (i= 0 3 6)

```
## 거꾸로 뒤집으려면 
## for i in range(0,n) -> for i in range(n, -1, -1)
``` python
a ='abcde'
for i in range (0, 5):
    print(a[i], end=' ')

for i in range(4, -1, -1): # 간격 -1
    print(a[i], end=' ') # e d c b a

print(a[::-1]) # 이게 제일 편하긴해~
```
