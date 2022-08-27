import sys
from collections import defaultdict
# 같은 숫자가 중복해서 들어있지 않음
def solution(matrix):
    n = len(matrix)
    answer = 0
    mDict = defaultdict(int)
    # 행
    for i in range(n):
        tmpList = sorted(matrix[i])
        mDict[tmpList[n//2]] += 1

    # 열
    for i in range(n):
        tmpList = []
        for j in range(n):
            tmpList.append(matrix[j][i])
        tmpList.sort()
        mDict[tmpList[n // 2]] += 1

    for value in mDict.values():
        if(value == 2):
            answer += 1
    return answer

print(solution(

[[1, 19, 20, 8, 25], [21, 4, 3, 17, 24], [12, 5, 6, 16, 15], [11, 18, 10, 9, 23], [7, 13, 14, 22, 2]]))