# https://www.acmicpc.net/problem/2559
n, m = map(int,input().split())
nums = [0]+list(map(int,input().split()))

for i in range(1,n+1):
    nums[i] += nums[i-1]

ans = -int(1e9)
for i in range(m, n+1):
    ans = max(ans,nums[i]-nums[i-m])
print(ans)
