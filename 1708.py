import sys
from math import atan2
input=sys.stdin.readline

def CCW(a,b,c,d): #vector ab, cd
    return a*d-c*b

def convex_hull(point):
    point.sort()
    base=point[0]
    point.sort(key=lambda x:(atan2(x[1]-base[1],x[0]-base[0]),(x[0]-base[0])**2+(x[1]-base[1])**2))
    point.remove(base)
    stack=[base,point[0]]
    for i in range(1,N-1):
        while len(stack)>=2 and CCW(stack[-1][0]-stack[-2][0],stack[-1][1]-stack[-2][1],point[i][0]-stack[-1][0],point[i][1]-stack[-1][1])<=0:
            stack.pop()
        stack.append(point[i])
    print(len(stack))

N=int(input())
point=[[*map(int,input().split())] for _ in range(N)]
convex_hull(point)
