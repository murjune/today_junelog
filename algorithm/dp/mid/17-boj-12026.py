# https://www.acmicpc.net/problem/12026
n = int(input())
arr = list(input())
d = [-1] * n
boj = "BOJ"
#  0 % 3
def dfs(now_idx, now_boj_idx, k):
    if now_idx == n: return

    next_boj_idx = (now_boj_idx + 1) % 3
    for i in range(now+1,n):

        if arr[i] == boj[next_boj_idx]:
            dist = (i - now_idx)
            dfs(now + dist,next_boj_idx, k + dist**2)
