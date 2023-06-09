import sys
from collections import deque

input=lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph=[list(input()) for _ in range(N)]
visited=[[False]*M for _ in range(N)]
dx,dy=[1,-1,0,0],[0,0,1,-1]

def find_I():
    for y in range(N):
        for x in range(M):
            if graph[y][x][0]=='I':
                return x, y

def bfs():
    dq=deque()
    x,y=find_I()
    dq.append((x,y))
    visited[y][x]=True
    ret=0
    while dq:
        x,y=dq.popleft()
        if graph[y][x]=='P':
            ret+=1
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<M and 0<=ny<N and not visited[ny][nx] and graph[ny][nx]!='X':
                visited[ny][nx]=True
                dq.append((nx,ny))
    if not ret:
        print('TT')
    else:
        print(ret)

bfs()