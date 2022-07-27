# combinations

(0~n-1)까지 list가 만들어 지는데, n//2로 짤라서 만들어지는 조합이 member에 저장
```python
from itertools import combinations

n = 6
member = list(combinations(range(0,n), n//2))
print(member)
# [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 2, 3), (0, 2, 4),
# (0, 2, 5), (0, 3, 4), (0, 3, 5), (0, 4, 5), (1, 2, 3),
# (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
```
