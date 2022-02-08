# 풀이
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
