def dfs(i, boj_idx):
    if i == 0:
        if boj[boj_idx] == "B":
            return 0
        else:
            return INF

    if d[i] < INF: return d[i]

    next_boj_idx = (boj_idx-1) % 3
    for j in range(i-1, -1, -1):
        if arr[j] == boj[next_boj_idx]:
            d[i] = min(d[i], dfs(j, next_boj_idx)+(i-j)**2)

    return d[i]
n = int(input())
arr = list(input())
INF = int(1e6) + 1
d = [INF] * n
boj = "BOJ"
LINK = boj.index(arr[-1])
# 0번은 반드시 B, 스타트
# n-1번에  링크
# 2에서 시작
#  Top-down방식
ans = dfs(n-1, LINK)
print(ans if ans < INF else -1)
# d[n] = min(d[n]+d[n-i] + (n-i)**2)

