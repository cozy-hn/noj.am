import sys
from collections import deque
input=lambda:sys.stdin.readline()
N,M=map(int,input().split())
Map=[list(map(int,input().split())) for _ in range(N)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def side_minus(x,y):
    s_dq=deque([(x,y)])
    Map[y][x]=-1
    while s_dq:
        x,y=s_dq.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=ny<N and 0<=nx<M and Map[ny][nx]==0:
                Map[ny][nx]=-1
                s_dq.append((nx,ny))

def check_cheeze(dq):
    flag=False
    for i in range(N):
        for j in range(M):
            air=0
            if Map[i][j]==1:
                for k in range(4):
                    nx,ny=j+dx[k],i+dy[k]
                    if 0<=ny<N and 0<=nx<M and Map[ny][nx]==-1:
                        air+=1
                if air>=2:
                    dq.append((j,i))
                    flag=True
    if flag:
        return True
    else:
        return False

side_minus(0,0)
dq=deque()
cnt=0
while check_cheeze(dq):
    cnt+=1
    while dq:
        x,y=dq.popleft()
        Map[y][x]=-1
        side_minus(x,y)
    print(*Map,sep='\n')
    print('-----------------')
print(cnt)

