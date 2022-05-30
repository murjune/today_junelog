# 부분수열의 합 14225
https://www.acmicpc.net/problem/14225

# 추가로 백트래킹으로도 풀 수 있다. 

# 1번째 풀이 : itertools의 combination 모듈

from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()
# 시간 복잡도 2^20 = 1_000_000 * 20 = 약 2000만
n = int(input()) # 1 ~ 20
# nums의 원소는 100,000보다 작거나 같은 자연수
nums = list(map(int,input().split()))
cache = [0]*(2_000_000 + 1)
# 숫자 배열 2_000_000

for i in range(1,n+1):
    for arr in list(combinations(nums,i)):
        cache[sum(arr)] = 1

for i in range(1,2_000_000 + 1):
    if cache[i] == 0:
        print(i)
        exit()
        

# 2번째 풀이 : 비트마스킹 (역시 더 빠르다)

from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()
# 시간 복잡도 2^20 = 1_000_000 * 20 = 약 2000만
n = int(input()) # 1 ~ 20
# nums의 원소는 100,000보다 작거나 같은 자연수
nums = list(map(int,input().split()))
cache = [0]*(2_000_000 + 1)
# 숫자 배열 2_000_000

for i in range(1, 1<<n): # 2^n - 1 의 경우의 수
    sum = 0
    for j in range(0, n): # 0 ~ n 자리수
        if(i & 1<<j):
            sum += nums[j]

        cache[sum] = 1

for i in range(1,2_000_000 + 1):
    if not cache[i]:
        print(i)
        break
     
