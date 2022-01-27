
deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

``` python
from collections import deque
# 1차원 배열
q =deque([1,2,3,4,5])


q.rotate(1) # 오른쪽으로 회전
print(q)

q.rotate(-1) # 왼쪽으로 회전
print(q)
```
