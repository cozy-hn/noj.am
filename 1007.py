import sys
from itertools import combinations

input=lambda:sys.stdin.readline()
for _ in range(int(input())):
    n=int(input())
    point=[tuple(map(int,input().split())) for _ in range(n)]
    combi=list(combinations(point,n//2))
    sum_x,sum_y=sum([x for x,y in point]),sum([y for x,y in point])
    ans=float('inf')
    for i in range(len(combi)//2):
        x1,y1=0,0
        for x,y in combi[i]:
            x1+=x
            y1+=y
        ans=min(ans,(sum_x-2*x1)**2+(sum_y-2*y1)**2)
    print(ans**0.5)