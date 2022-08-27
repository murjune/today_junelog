from itertools import permutations


#적어도 선분 2개 사용해서 점을 덮어야함
# O(10!) = 362만
# dots최대 길이 20 , O(7240만)...
# lines길이 10, O(7억)...
INF = int(1e9)
def solution(dots: list, lineList: list):
    if(len(lineList) == 1):#선분길이가 1이면 안되니까
return -1
    ans = INF
    dots_len = len(dots)
    for lines in list(permutations(lineList)):
        dot_idx = 0
        cnt = 0
        now = dots[0]
        for line in lines:
            cnt += 1
            now += line
            while (dot_idx < dots_len and dots[dot_idx] <= now):
                dot_idx += 1
            if(dot_idx == dots_len):
                ans = min(ans, cnt)
                break
            now = dots[dot_idx]
    if(ans == 1):
        ans = 2
    elif(ans == INF):
        ans = -1
    return ans