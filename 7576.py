import sys
from collections import deque
input= lambda : sys.stdin.readline().rstrip()
M,N=map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
dq=deque()
tomato=0
empty=0
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            tomato+=1
        if graph[i][j]==-1:
            empty+=1
        if graph[i][j]==1:
            dq.append((i,j,0))
dx=[1,0,-1,0]
dy=[0,1,0,-1]
# print("tomato : ",tomato)
# print("empty : ",empty)
if tomato+empty==N*M:
    print(-1)
else:
    while dq:
        o=dq.popleft()
        for i in range(4):
            tmpx=o[1]+dx[i]  
            tmpy=o[0]+dy[i]
            if 0<=tmpx<M and 0<=tmpy<N and graph[tmpy][tmpx]==0:
                graph[tmpy][tmpx]=o[2]+1
                dq.append((tmpy,tmpx,o[2]+1))
                tomato-=1
    day=o[2]
    if tomato:
        print(-1)
    else:
        print(day)