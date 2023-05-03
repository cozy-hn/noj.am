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
line = [list(map(int, input().split())) for _ in range(N)]
Map=[[-1]*N for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        if i==j:
            Map[i][j]=3
        else:
            Map[i][j]=ex(line[i][0],line[i][1],line[i][2],line[i][3],line[j][0],line[j][1],line[j][2],line[j][3])
            Map[j][i]=Map[i][j]
for i in range(N):
    print(*Map[i],sep='')