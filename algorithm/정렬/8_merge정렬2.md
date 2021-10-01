https://github.com/murjune/today_junelog/blob/main/algorithm/%EC%A0%95%EB%A0%AC/7_merge%EC%A0%95%EB%A0%AC.md
위와 같이 하면 시간 error가 뜬다...  
이유는 잘 모르겠다. 
# 가장 빠른 머지정렬 소스코드
``` python
def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0

    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k+=1
    
    if i==len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j==len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

```
