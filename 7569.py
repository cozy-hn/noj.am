import sys
from collections import deque
input= lambda : sys.stdin.readline().rstrip()
M,N,H=map(int,input().split())
graph=[[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        graph[i].append(list(map(int,input().split())))
dq=deque()
tomato=0
empty=0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j]==0:
                tomato+=1
            if graph[k][i][j]==-1:
                empty+=1
            if graph[k][i][j]==1:
                dq.append((i,j,k))
dx=[1,0,-1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]
# print("tomato : ",tomato)
# print("empty : ",empty)
if tomato+empty==N*M*H:
    print(-1)
else:
    while dq:
        y,x,z=dq.popleft()
        for i in range(6):
            tmpx=x+dx[i]  
            tmpy=y+dy[i]
            tmph=z+dz[i]
            if 0<=tmpx<M and 0<=tmpy<N and 0<=tmph<H and graph[tmph][tmpy][tmpx]==0:
                graph[tmph][tmpy][tmpx]=graph[z][y][x]+1
                dq.append((tmpy,tmpx,tmph))
                tomato-=1
                
    if tomato:
        print(-1)
    else:
        print(graph[z][y][x]-1)