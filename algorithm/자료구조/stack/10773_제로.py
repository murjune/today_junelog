import sys

input = lambda: sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(str(x) + "\n")

stack = []
cnt = 0

for i in range(int(input())):

    cur = int(input())

    if(cur == 0):
        if(stack):
            cnt -= stack[-1]
            stack.pop()
    else:
        cnt += cur
        stack.append(cur)

print(cnt)
