# 문제 : [Abbreviation](https://www.hackerrank.com/challenges/abbr/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming)  


# 풀이

먼저 재귀함수를 만들어 문제를 풀었는데, testcase 5 6 11 12 13이 시간초과로 통과하지 않아  
메모이제이션 기법을 활용하여 재귀함수를 개선하였고, 즉 탑 다운식으로 문제를 풀었다.  

```python
#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**6)

def Search(a, b):# boolen
    # 메모이제이션 
    # dp테이블의 값이 0이상이면 dp테이블에 저장된값 가져오기
    if d[len(a)][len(b)] >= 0: return d[len(a)][len(b)]
    
    # 재귀함수 break
    if not a or not b:
        if not a and b: 
            d[len(a)][len(b)] = False
            return d[len(a)][len(b)]
        if a and not b: 
            d[len(a)][len(b)] = True
            return d[len(a)][len(b)]
        if not a and not b: 
            d[len(a)][len(b)] = True
            return d[len(a)][len(b)]
    
    
    # B = B (마지막 알파벳이 같을 경우)
    if a[-1] == b[-1]:
        d[len(a)][len(b)] = Search(a[:-1], b[:-1]) 
        return d[len(a)][len(b)]
    
    # a의 마지막 알파벳이 소문자일 경우 - (즉 삭제 가능한 경우)
    elif a[-1].islower():
        # a의 마지막 알파벳과 b의 마지막 알파벳이 일치
        # b = B
        if chr(ord(a[-1])-32) == b[-1]:
            d[len(a)][len(b)] = (True if (Search(a[:-1],b[:-1])or Search(a[:-1],b)) else False)
            return d[len(a)][len(b)]
        # a의 마지막 알파벳과 b의 마지막 알파벳이 다를 경우
        # c = B
        else:
            d[len(a)][len(b)] = Search(a[:-1],b)
            return d[len(a)][len(b)]
            
    # a의 마지막 알파벳이 대문자이고, b의 불일치       
    # A -> B로 바꾸는 것이 불가능!
    # A != B, can't remove A
    d[len(a)][len(b)] = False
    return d[len(a)][len(b)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()
        d = [[-1]*(len(b)+1) for _ in range(len(a)+1)]
        ans = Search(a, b)
        result = ("YES" if ans else "NO")
        
        fptr.write(result + '\n')

    fptr.close()

```
