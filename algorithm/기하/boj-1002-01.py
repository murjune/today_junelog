
for _ in range(int(input())):
    x1,y1, r1, x2,y2,r2 = map(int,input().split())

    dist = (x1-x2)**2 + (y1-y2)**2
    pivot = (r1+r2)**2

    if pivot == dist:
        print(1)
    elif pivot > dist:
        print(2)
    else:
        print(0)
