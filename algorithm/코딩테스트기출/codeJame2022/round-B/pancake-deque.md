# [Pancake Deque](https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd59d)
# 풀이 1
```python

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
write = lambda x : sys.stdout.write(str(x)+ "\n")


for i in range(int(input())):
    # like MST
    # popleft() or pop()
    n = int(input())
    q = deque(map(int,input().split()))
    cnt = 0
    tmp = -1
    while q:
        if q[0] <= q[-1]:
            if q[0] >= tmp:
                cnt += 1
            tmp = max(tmp, q.popleft())
        else:
            if q[-1] >= tmp:
                cnt +=1
            tmp = max(tmp, q.pop())
    write("Case #{0}: {1}".format(i + 1, cnt))


```
# 풀이 2
```python

from collections import deque


for i in range(int(input())):
    # like MST
    # popleft() or pop()
    n = int(input())
    q = deque(map(int,input().split()))
    cnt = 0
    tmp = -1
    while q:
        if tmp <= q[0] and tmp <= q[-1]:
            if q[0] < q[-1]:
                tmp = q.popleft()
                cnt += 1
            else:
                tmp = q.pop()
                cnt += 1
        elif q[-1]< tmp <= q[0]:
            q.pop()
        elif q[0]<tmp <= q[-1]:
            q.popleft()
        else:
            if q[0] < q[-1]:
                q.pop()
            else:
                q.popleft()
    print("Case #{0}: {1}".format(i + 1, cnt))
```
