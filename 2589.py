import sys
from collections import deque

def bfs(a,b):
    visit=[[0]*M for _ in range(N)]
    dq=deque([(a,b)])
    visit[b][a]=1
    while dq:
        x,y=dq.popleft()
        visitnum=visit[y][x]
        for k in range(4):
            tmpx=x+dx[k]
            tmpy=y+dy[k]
            if 0<=tmpx<M and 0<=tmpy<N and visit[tmpy][tmpx]==0 and graph[tmpy][tmpx]=='L':
                dq.append((tmpx,tmpy))
                visit[tmpy][tmpx]=visitnum+1
    return visitnum-1

input=lambda:sys.stdin.readline().rstrip()
N,M=map(int,input().split())
graph=[list(input()) for _ in range(N)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans=0
for i in range(N):
    for j in range(M):
        if graph[i][j]=='L':
            check=bfs(j,i)
            if ans<check:
                ans=check
print(ans)