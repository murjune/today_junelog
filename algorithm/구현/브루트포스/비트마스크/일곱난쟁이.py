# https://www.acmicpc.net/problem/2309  
# 비트마스킹

import sys

input = lambda: sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x) + "\n")
# 100 1011 & 100
arr = list(int(input()) for _ in range(9))

arr.sort(reverse=True)
for i in range(1, 1<<9):
    sum = 0
    if(format(i, 'b').count('1') == 7):
        for j in range (9):
            if((1<<j & i) > 0) :
                sum += arr[8-j]

        if(sum == 100):
            for j in range(9):
                if((1 <<j & i) > 0) :
                    print(arr[8-j])
            break



