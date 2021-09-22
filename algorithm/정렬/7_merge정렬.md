참고 블로그: https://ratsgo.github.io/data%20structure&algorithm/2017/10/03/mergesort/
참고 강의_동빈나: https://www.youtube.com/watch?v=ctkuGoJPmAE&t=120s
# 머지 정렬- 재귀함수 이용
![image](https://user-images.githubusercontent.com/87055456/134309279-42bfc9b2-0e1c-4a47-b574-7ba4936e7337.png)

시간복잡도: 너비가 N 높이가 logN번 이기 때문에 시간 복잡도 O(N * logN)을 보장한다.

## merge_sort 함수
```
합병정렬을 파이썬으로 구현한 코드는 다음과 같다.

1) 우선 주어진 리스트를 중간 지점인 mid(𝑞)를 중심으로 왼쪽 리스트(leftList)와 오른쪽 리스트(rightList)로 쪼갠다.
2) leftList와 rightList 각각에 다시 이 작업을 재귀적으로 적용한다.
3) 분리된 리스트를 합치는 merge 함수는 주어진 두 개 리스트를 크기 순으로 정렬하는 역할을 한다.
```
merge_sort 함수의 파이썬 코드는 다음과 같다.
``` python
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)
```

## merge 함수
```
분리된 리스트를 합치는 merge 함수는 다음과 같습니다.

1) 위에서 분리한 왼쪽 리스트(left)와 오른쪽 리스트(right)의 첫번째 요소를 비교해 작은 값을 결과 리스트(result)에 저장해 놓고, 
해당 값을 해당 리스트에서 지웁니다. 

2) 이를 left와 right의 요소가 하나도 없을 때까지 반복합니다.
```

merge 함수의 파이썬 코드는 다음과 같다.
``` python
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
```

## 예시
``` python
number_list = [21, 10, 12, 20, 25, 13, 15, 22]

# left= [21, 10, 12, 20] right = [25, 13, 15, 22]

# 합병 함수
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0: # left, right 리스트의 길이가 0일때까지 반복

        if len(left) > 0 and len(right) > 0: # left의 길이가 right길이 보다 길때

            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:] # 인덱싱을 통해 left[0]을 제거

            else: # left[0] > right[0]
                result.append(right[0])
                right = right[1:] # 인덱싱을 통해 right[0]을 제거

        elif len(left) > 0: # len(right ) == 0
            result.append(left[0])
            left = left[1:]

        elif len(right) > 0: # len(left) == 0
            result.append(right[0])
            right = right[1:]

    return result #  # 합변

# 합병 정렬 함수

def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2 # 4

    left_List = list[:mid] # [21,10, 12, 20] 

    right_List = list[mid:] # [25, 13, 15, 22] 

    left_List = merge_sort(left_List) # 앞 쪽 부분 정렬

    right_List = merge_sort(right_List) # 뒷 쪽 부분 정렬

    return merge(left_List, right_List) # 병합

print(merge_sort(number_list))
# [10, 12, 13, 15, 20, 21, 22, 25]
```
