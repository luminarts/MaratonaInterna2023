x1, y1, x2, y2 = [int(i) for i in input().split()]



if x1 > x2:
    print(0)
elif y1 > y2:
    z = (x2-x1)/(y1-y2)
    k = int(z)
    print(k+1)
elif y1 < y2:
    print(-1)

