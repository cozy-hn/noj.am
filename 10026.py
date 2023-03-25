import sys
from collections import deque

def bfs(N,graph):
    cnt=0
    for i in range(N):
        for j in range(N):
            if graph[i][j]!='D':
                cnt+=1
                char=graph[i][j]
                dq=deque([(j,i)])
                graph[i][j]='D'
                while dq:
                    x,y=dq.popleft()
                    for k in range(4):
                        tmpx=x+dx[k]
                        tmpy=y+dy[k]
                        if 0<=tmpx<N and 0<=tmpy<N and graph[tmpy][tmpx]==char:
                            dq.append((tmpx,tmpy))
                            graph[tmpy][tmpx]='D'

    return cnt

input=lambda:sys.stdin.readline().rstrip()
N=int(input())
graph1=[list(input()) for _ in range(N)]
graph2=[i[:] for i in graph1]
for i in range(N):
    for j in range(N):
        if graph2[i][j]=='G':
            graph2[i][j]='R'
dx=[1,-1,0,0]
dy=[0,0,1,-1]
print(bfs(N,graph1),bfs(N,graph2))