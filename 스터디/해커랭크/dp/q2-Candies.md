# 풀이 1   
수열을 선형 탐색하면서, 
- case 1: c[i-1] < c[i] (=오름차순)인 경우를 만나면 d[i] = d[i-1] + 1로 dp테이블을 갱신해준다.  
    > 1-1 : stack(증가하지 않는 부분 순열)에 원소가 있으면, stack을 for문으로 돌며 dp 테이블 갱신  
    > 1-2 : stack = []으로 초기화 해주고, d[i] = d[i-1] + 1로 갱신  
- case 2: c[i-1] >= c[i]인 증가하지 않는 부분 수열을 stack에 담는다.  

- case 3: 수열의 선형 탐색이 끝나면, 남은 stack 1-1과정 수행


```python

n = int(input())
c = [0]+[int(input()) for _ in range(n)]
d = [0]+[1]*n
stack = []
flag = 0

for i in range(1 , n +1):
    if c[ i -1] < c[i]:
        ##############
        if stack:
            l = len(stack)
            stack = stack[::-1]
            for j in range(1 ,l):
                if stack[ j -1][1] < stack[j][1]:
                    d[stack[j][0]] = max(d[stack[j][0]], d[stack[ j -1][0] ] +1)
                elif stack[ j -1][1] == stack[j][1] and c[stack[j][0]-1]>= c[stack[j][0]]:
                    d[stack[j][0]] = 1
            ## init
            flag = 0 # flag init
            stack = [] # stack init
        #############
        d[i] = d[ i -1] + 1


    # descending Sequence-> Stack push
    elif c[ i -1] >= c[i]:
        if not flag:
            stack.append(( i -1 ,c[ i -1]))
            stack.append((i ,c[i]))
            flag = 1
        else:
            stack.append((i ,c[i]))

if stack:
    l = len(stack)
    stack = stack[::-1]
    for j in range(1 ,l):

        if stack[ j -1][1] < stack[j][1]:
            d[stack[j][0]] = max(d[stack[j][0]], d[stack[ j -1][0] ] +1)
        elif stack[ j -1][1] == stack[j][1] and c[stack[j][0]-1]>= c[stack[j][0]]:
            d[stack[j][0]] = 1

print(sum(d))
```

# 풀이 2 - 훨씬 쉬운 풀이..  
1. left -> right로 수열을 선형 탐색하며 오름차순인 부분 수열을 조건에 맞게 dp테이블 갱신  
2. 이번에는 right -> left로 수열을 선형 탐색하며 증가하지 않는 부분 수열을 조건에 맞게 dp테이블 갱신
```python

n = int(input())
c = [0]+[int(input()) for _ in range(n)]
d = [0]+[1]*n

# ascend
for i in range(1 , n +1):
    if c[ i -1] < c[i]:
        d[i] = d[i-1] + 1

# descend
for i in range(n,0,-1):
    if c[i] < c[i-1]:
        d[i-1] =max(d[i-1], d[i] + 1)
    elif c[i] == c[i-1] and d[i-1] == 1:
        d[i-1] = 1

print(sum(d))
```
