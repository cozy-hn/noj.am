import sys
input=sys.stdin.readline
def det(a,b,c,d):
    if a*d-c*b > 0:
        return 1
    elif a*d-c*b < 0:
        return -1
    else:
        return 0


def ex(x1,y1,x2,y2,x3,y3,x4,y4):
    v1,v2,v3,v4=x2-x1,y2-y1,x4-x3,y4-y3

    a=det(v1,v2,x3-x1,y3-y1)
    b=det(v1,v2,x4-x1,y4-y1)
    c=det(v3,v4,x1-x3,y1-y3)
    d=det(v3,v4,x2-x3,y2-y3)
    if a*b < 0 and c*d < 0:
        return(2)
    elif a*b*c*d == 0:
        if a==0 and c==0:
            if x1==x3 and y1==y3 and b!=0:
                return (1)
            if (x1==x3 and y1==y3 and x2==x4 and y2==y4) or (x1==x4 and y1==y4 and x2==x3 and y2==y3):
                return(3)
            elif x1==x2==x3==x4:
                if min(y1,y2) < y3 < max(y1,y2) or min(y1,y2) < y4 < max(y1,y2) or min(y3,y4) < y1 < max(y3,y4) or min(y3,y4) < y2 < max(y3,y4):
                    return(3)
                elif min(y1,y2)==max(y3,y4) or min(y3,y4)==max(y1,y2):
                    return(1)
                else:
                    return(0)
            elif min(x1,x2)==max(x3,x4) or min(x3,x4)==max(x1,x2):
                return(1)
            elif min(x1,x2) <= x3 <= max(x1,x2) or min(x1,x2) <= x4 <= max(x1,x2) or min(x3,x4) <= x1 <= max(x3,x4) or min(x3,x4) <= x2 <= max(x3,x4):
                return(3)
            else:
                return(0)
        elif a==0:
            if x1==x2:
                if min(y1,y2)<y3<max(y1,y2):
                    return(1)
                if y3==y1 or y3==y2:
                    return(1)
                else:
                    return(0)
            if min(x1,x2) < x3 < max(x1,x2):
                return(1)
            elif x3==x1 or x3==x2:
                return (1)
            else:
                return(0)
        elif b==0:
            if x1==x2:
                if min(y1,y2)<y4<max(y1,y2):
                    return(1)
                if y4==y1 or y4==y2:
                    return(1)
                else:
                    return(0)
            if min(x1,x2) < x4 < max(x1,x2):
                return(1)
            elif x4==x1 or x4==x2:
                return (1)
            else:
                return(0)
        elif c==0:
            if x3==x4:
                if min(y3,y4)<y1<max(y3,y4):
                    return(1)
                if y1==y3 or y1==y4:
                    return(1)
                else:
                    return(0)
            if min(x3,x4) < x1 < max(x3,x4):
                return(1)
            elif x1==x3 or x1==x4:
                return (1)
            else:
                return(0)
        elif d==0:
            if x3==x4:
                if min(y3,y4)<y2<max(y3,y4):
                    return(1)
                if y2==y3 or y2==y4:
                    return(1)
                else:
                    return(0)
            if min(x3,x4) < x2 < max(x3,x4):
                return(1)
            elif x2==x3 or x2==x4:
                return (1)
            else:
                return(0)
    else:
        return(0)

N=int(input())
for i in range(N):
    xm, ym, xM, yM, x1,y1,x2,y2=*map(int, input().split()), *map(int, input().split())
    a,b,c,d=ex(xm,ym,xM,ym,x1,y1,x2,y2),ex(xM,ym,xM,yM,x1,y1,x2,y2),ex(xM,yM,xm,yM,x1,y1,x2,y2),ex(xm,yM,xm,ym,x1,y1,x2,y2)
    if a==0 and b==0 and c==0 and d==0:
        print(0)
    elif a==3 or b==3 or c==3 or d==3:
        print(4)
    else:
        ans=0
        cnt=0
        if a==2:
            ans+=1
        elif a==1:
            if not ((y1==ym and xm<x1<xM) or (y2==ym and xm<x2<xM)):
                cnt+=1
            ans+=1
        if b==2:
            ans+=1
        elif b==1:
            if not ((x1==xM and ym<y1<yM) or (x2==xM and ym<y2<yM)):
                cnt+=1
            ans+=1
        if c==2:
            ans+=1
        elif c==1:
            if not ((y1==yM and xm<x1<xM) or (y2==yM and xm<x2<xM)):
                cnt+=1
            ans+=1
        if d==2:
            ans+=1
        elif d==1:
            if not ((x1==xm and ym<y1<yM) or (x2==xm and ym<y2<yM)):
                cnt+=1
            ans+=1
        print(ans-cnt//2)