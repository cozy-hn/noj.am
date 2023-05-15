import sys
from collections import deque

input = sys.stdin.readline
N,M=map(int,input().split())
MAP=[[*map(int,list(input().rstrip()))] for _ in range(N)]
visit=[[0]*M for _ in range(N)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
SET=0
SETDIC={}

def bfs(x,y):
    global SET, SETDIC
    SET-=1
    dq=deque([(x,y)])
    visit[y][x]=SET
    cnt=1
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<M and 0<=ny<N and MAP[ny][nx]==0 and not visit[ny][nx]:
                visit[ny][nx]=SET
                cnt+=1
                dq.append((nx,ny))
    SETDIC[SET]=cnt
    return cnt

for i in range(N):
    for j in range(M):
        if MAP[i][j]==0 and not visit[i][j]:
            bfs(j,i)

for i in range(N):
    for j in range(M):
        if MAP[i][j]==1:
            ans=1
            tmpset=set()
            for k in range(4):
                nx,ny=j+dx[k],i+dy[k]
                if 0<=nx<M and 0<=ny<N and MAP[ny][nx]==0:
                    tmpset.add(visit[ny][nx])
            for k in tmpset:
                ans+=SETDIC[k]
            print(ans%10,end='')
        else:
            print(0,end='')
    print()
