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
