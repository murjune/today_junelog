# 입출력

알고리즘 문제를 풀때  
특히 정렬, 이진탐색 등등 느린 입출력을 써서 시간 초과나 메모리 초과가 일어나는 경우가 있다.  
따라서, input -> sys.stdin.readline, print -> sys.stdout.write으로 풀자!!

## 응용
편의를 위해 lamda함수를 이용하여 read를 input처럼 write를 print 처럼 쓰도록 사용자화 하였다.
``` python

import sys

read = lambda : sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x)+ "\n")

```
