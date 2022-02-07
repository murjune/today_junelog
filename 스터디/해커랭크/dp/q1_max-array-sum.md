# 문제: [max-array-sum](https://www.hackerrank.com/challenges/max-array-sum/problem)  

문제 조건이 subset의 길이가 1보다 커야된다고(2 이상)이라고 이해해서, 엄청 삽질한 문제..  

# 풀이  
전형적인 바텀-업 풀이. 
```
1. i번째 원소 미 포함: d[i-1] or d[i-2]
2. i번째 원소 포함 : d[i-2]+nums[i], nums[i](d[i-2]가 음수일 수 있으므로) 
```
점화식 : d[i] = max(nums[i], d[i-1], d[i-2], d[i-2]+nums[i]). 

- d[0],d[1]을 nums[0], max(d[0], nums[1])로 초기값을 세팅해준다.  
- 반복문을 돌며, (0~i)구간의 최댓값을 구해 d테이블에 갱신해준다.  
```python
def maxSubsetSum(nums):
    
    d = [0]*(n)
    #  초깃값 세팅
    d[0] = nums[0]
    for i in range(1,n):
        if i == 1 :
            d[i] = max(d[i-1],nums[i])
            continue
        # i >= 2, 점화식
        tmp = d[i-2] + nums[i]
        tmp2 = d[i-2]
        tmp3 = d[i-1]
        tmp4 = nums[i]
        d[i] = max(tmp,tmp2,tmp3,tmp4)
    
    
    ans = max(d)
    return max(ans,0)
```
