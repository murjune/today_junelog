# https://www.acmicpc.net/problem/1002

for _ in range(int(input())):
    x1,y1, r1, x2,y2,r2 = map(int,input().split())

    dist = (x1-x2)**2 + (y1-y2)**2
    pivot1 = (r1+r2)**2
    pivot2 = (r1-r2)**2

    if pivot2 < dist < pivot1:
        print(2)
    elif dist == pivot1:
        print(1)
    elif dist > pivot1:
        print(0)
    elif pivot2 > dist:
        print(0)
    elif pivot2 == dist:
        if (x1,y1) == (x2, y2):
            print(-1)
        else:
            print(1)

