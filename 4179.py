import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

R,C=map(int,input().split())
maze=[list(input()) for _ in range(R)]
dqj=deque()
dqf=deque()
for i in range(R):
    for j in range(C):
        if maze[i][j]=='J':
            dqj.append((j,i,0))
            if j==0 or i==0 or j==C-1 or i==R-1:
                print(1)
                sys.exit()
            maze[i][j]='.'
        elif maze[i][j]=='F':
            dqf.append((j,i,0))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while dqj:
    xj,yj,time=dqj.popleft()
    while dqf and dqf[0][2]==time:
        xf,yf,time=dqf.popleft()
        for i in range(4):
            nxf=xf+dx[i]
            nyf=yf+dy[i]
            if 0<=nxf<C and 0<=nyf<R and maze[nyf][nxf]=='.':
                maze[nyf][nxf]='F'
                dqf.append((nxf,nyf,time+1))
    for i in range(4):
        nxj=xj+dx[i]
        nyj=yj+dy[i]
        if 0<=nxj<C and 0<=nyj<R and maze[nyj][nxj]=='.':
            if nyj==0 or nyj==R-1 or nxj==0 or nxj==C-1:
                print(time+2)
                sys.exit()
            maze[nyj][nxj]='J'
            dqj.append((nxj,nyj,time+1))
print('IMPOSSIBLE')