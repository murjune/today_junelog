# https://www.acmicpc.net/problem/2629
import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()
def dfs(idx,r,l) :
    w = abs(r-l)
    if not df[w]:
        df[w] = 1
    if idx == n : return
    if d[idx][w] == 0:
        # 오른쪽 저울
        dfs(idx+1, r + weights[idx], l)
        # 저울에 올리지 않음
        dfs(idx + 1, r, l)
        # 왼쪽 저울
        dfs(idx + 1, r, l+ weights[idx])
        d[idx][w] = 1

n = int(input())
weights = list(map(int,input().split()))
marble = int(input())
marbles = list(map(int,input().split()))
df = defaultdict(int)
d = [[0]*15001 for i in range(n+1)]

dfs(0,0,0)
ans =[]
for m in marbles:
    ans.append('Y') if df[m] else ans.append('N')

print(' '.join(ans))
