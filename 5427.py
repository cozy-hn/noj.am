import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())):
    flag=True
    C,R=map(int,input().split())
    maze=[list(input()) for _ in range(R)]
    dqj=deque()
    dqf=deque()
    for i in range(R):
        for j in range(C):
            if maze[i][j]=='@':
                dqj.append((j,i,0))
                if j==0 or i==0 or j==C-1 or i==R-1:
                    print(1)
                    flag=False
                    break
                maze[i][j]='.'
            elif maze[i][j]=='*':
                dqf.append((j,i,0))
        if flag==False:
            break
    if flag==False:
        continue
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while dqj:
        xj,yj,time=dqj.popleft()
        maze[yj][xj]='-'
        while dqf and dqf[0][2]==time:
            xf,yf,time=dqf.popleft()
            for i in range(4):
                nxf=xf+dx[i]
                nyf=yf+dy[i]
                if 0<=nxf<C and 0<=nyf<R and maze[nyf][nxf]=='.':
                    maze[nyf][nxf]='*'
                    dqf.append((nxf,nyf,time+1))
        for i in range(4):
            nxj=xj+dx[i]
            nyj=yj+dy[i]
            if 0<=nxj<C and 0<=nyj<R and maze[nyj][nxj]=='.':
                if nyj==0 or nyj==R-1 or nxj==0 or nxj==C-1:
                    print(time+2)
                    flag=False
                    break
                maze[nyj][nxj]='@'
                dqj.append((nxj,nyj,time+1))
        if flag==False:
            break
    if flag==True:
        print('IMPOSSIBLE')