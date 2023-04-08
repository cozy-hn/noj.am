import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

N,M=map(int,input().split())
if N==1 and M==1:
    print(1)
    sys.exit()
Map=[list(map(int,list(input()))) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
dq=deque([(0,0,0,1)])
visited[0][0]=1
dx=[1,0,-1,0]
dy=[0,1,0,-1]

while dq:
    x,y,b,n=dq.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx==N-1 and ny==M-1:
            print(n+1)
            sys.exit()
        if 0<=nx<N and 0<=ny<M and (visited[nx][ny]==0 or visited[nx][ny]==2):
            if Map[nx][ny]==0 and b==0:
                visited[nx][ny]=1
                dq.append((nx,ny,0,n+1))
            elif Map[nx][ny]==0 and b==1 and visited[nx][ny]==0:
                visited[nx][ny]=2
                dq.append((nx,ny,1,n+1))
            elif Map[nx][ny]==1 and b==0:
                visited[nx][ny]=2
                dq.append((nx,ny,1,n+1))
else:
    print(-1)