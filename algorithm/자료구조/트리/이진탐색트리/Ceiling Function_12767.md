# 문제: Ceiling Function

https://www.acmicpc.net/problem/12767. 

bst의 구현 + pre_order 순회
# 풀이
``` python
class Node():
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        # 만약 루트 노드가 없다면
        if self.root is None:
            self.root = Node(value)
            return

        self.now = self.root
        while True:

            if value < self.now.node:
                if self.now.left == None:
                    self.now.left = Node(value)

                    break
                else:
                    self.now = self.now.left
            else:
                if self.now.right == None:
                    self.now.right = Node(value)

                    break
                else:
                    self.now = self.now.right


def pre_order(now):
    global ans
    ans += 'N' # now 노드에 방문
    if now == None:
        return

    if now.left:
        ans += 'L' # 왼쪽 간선으로 들어감
        pre_order(now.left)
        ans += 'l' # 왼쪽 간선으로 나감
    if now.right:
        ans += 'R' # 오른쪽 간선으로 들어감
        pre_order(now.right)
        ans += 'r' # 오른쪽 간선으로 나감

import  sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
ans_arr = set()
for _ in range(n):
    arr = list(map(int, input().split()))
    bst = BST()
    for i in arr:
        bst.insert(i)
    ans = ''
    pre_order(bst.root)
    ans_arr.add(ans)

print(len(ans_arr))
```
