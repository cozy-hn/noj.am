x1,y1,x2,y2,x3,y3,x4,y4=map(int,open(0).read().split())
v1,v2,v3,v4=x2-x1,y2-y1,x4-x3,y4-y3

def det(a,b,c,d):
    if a*d-c*b > 0:
        return 1
    elif a*d-c*b < 0:
        return -1
    else:
        return 0
a=det(v1,v2,x3-x1,y3-y1)
b=det(v1,v2,x4-x1,y4-y1)
c=det(v3,v4,x1-x3,y1-y3)
d=det(v3,v4,x2-x3,y2-y3)

if a*b < 0 and c*d < 0:
    print(1)
elif a*b*c*d == 0:
    if a==0 and c==0:
        if x1==x2==x3==x4:
            if min(y1,y2) <= y3 <= max(y1,y2) or min(y1,y2) <= y4 <= max(y1,y2) or min(y3,y4) <= y1 <= max(y3,y4) or min(y3,y4) <= y2 <= max(y3,y4):
                print(1)
            else:
                print(0)
        elif min(x1,x2) <= x3 <= max(x1,x2) or min(x1,x2) <= x4 <= max(x1,x2) or min(x3,x4) <= x1 <= max(x3,x4) or min(x3,x4) <= x2 <= max(x3,x4):
            print(1)
        else:
            print(0)
    elif a==0:
        if min(x1,x2) <= x3 <= max(x1,x2):
            print(1)
        else:
            print(0)
    elif b==0:
        if min(x1,x2) <= x4 <= max(x1,x2):
            print(1)
        else:
            print(0)
    elif c==0:
        if min(x3,x4) <= x1 <= max(x3,x4):
            print(1)
        else:
            print(0)
    elif d==0:
        if min(x3,x4) <= x2 <= max(x3,x4):
            print(1)
        else:
            print(0)
else:
    print(0)