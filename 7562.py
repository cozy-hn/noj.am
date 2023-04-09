import sys
from collections import deque
input = lambda: sys.stdin.readline()

def bfs(Map,x1,y1,x2,y2):
    if x1==x2 and y1==y2:
        return 0
    dq=deque([(x1,y1,0)])
    while dq:
        x,y,cnt=dq.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if nx==x2 and ny==y2:
                return cnt+1
            if 0<=nx<l and 0<=ny<l and Map[nx][ny]==0:
                Map[nx][ny]=1
                dq.append((nx,ny,cnt+1))


dx=[2,1,-1,-2,-2,-1,1,2]
dy=[1,2,2,1,-1,-2,-2,-1]       
for _ in range(int(input())):
    l=int(input())
    Map=[[0]*l for _ in range(l)]
    print(bfs(Map,*map(int,input().split()),*map(int,input().split())))
    