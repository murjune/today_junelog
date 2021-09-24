# 예제2: 주어진 성과 이름에서 각 성에 어떤 이름이 있는지 분류하는 것이다.

풀이
``` python

# defaltdict() 사용

from  collections import defaultdict

name_list = [('Lee', 'JW'), ('Yang', 'JW'), ('Lee', 'MG'), ('Kim', 'KJ')]

name_dic = defaultdict(list)

for k, v in name_list: # 리스트의 요소가 튜플이기 때문에 k, v 값으로 할당
    name_dic[k].append(v) # 값이 list이기 때문에 append() 이용해서 항목 추가

print(name_dic)
# defaultdict(<class 'list'>, {'Lee': ['JW', 'MG'], 'Yang': ['JW'], 'Kim': ['KJ']})

```
