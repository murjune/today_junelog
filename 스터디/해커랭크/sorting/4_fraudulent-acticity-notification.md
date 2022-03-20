# Fraudulent Activity Notifications

# 오답 풀이 : 시간초과..  
시간 초과가 된다는 것은 알고 있지만, 일단 아이디어가 떠오르지 않아 구현해보았다.
```python
# boolean method
def median(arr, d, today_expenditure):
    if d % 2 == 1:
        tmp = arr[d // 2]
    elif d % 2 == 0:
        tmp = (arr[d // 2] + arr[d // 2 - 1]) / 2

    return False if (today_expenditure < tmp*2) else True


def activityNotifications(arr, d):
    # Write your code here
    cnt = 0
    start = 0
    stack = []
    for i in range(d, n ):
        stack = sorted(arr[start:i])
        if (median(stack, d, arr[i])): cnt += 1
        start+=1
    return cnt
```
# 오답풀이 2
```python

def activityNotifications(arr, d):
    
    # arr = [2 3 4 2 3 6 8 4 5]
    cnt = 0
    
    stack = []
    for i in range(d):
        stack.append((i,arr[i]))
    stack.sort(key = lambda x : x[1])
    # stack = [(0,2)(3,2)(1,3)(4,3)(2,4)]

    for i in range(d, n): # d = 5
        now_idx, now_val = i, arr[i]
        if d % 2 == 1:
            tmp = stack[d // 2][1]
        elif d % 2 == 0:
            tmp = (stack[d // 2][1] + stack[d // 2 - 1][1]) / 2
            
        if (now_val >= tmp*2): 
            cnt += 1
        stack2 = []
        flag = False
        
        for idx,val in stack:
            if idx == (i-d): continue
            if val <= now_val:
                stack2.append((idx,val))
            else:
                if flag:
                    stack2.append((idx,val))
                else:
                    stack2.append((now_idx, now_val))
                    stack2.append((idx,val))
                    flag = True
        if not flag:
            stack2.append((now_idx, now_val))
        stack = stack2[:]
        
    return cnt


# 풀이

n,d = map(int,input().split())
arr = list(map(int,input().split()))
print(activityNotifications(arr,d))
```
