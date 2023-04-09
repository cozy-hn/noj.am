def det(a,b,c,d):
    if a*d-c*b > 0:
        return 1
    elif a*d-c*b < 0:
        return -1
    else:
        return 0

x1,y1,x2,y2,x3,y3 = map(int,open(0).read().split())
print(det(x2-x1,y2-y1,x3-x2,y3-y2))
