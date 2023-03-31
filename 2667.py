from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()
N=int(input())
graph=[list(map(int,list(input()))) for _ in range(N)]
dange=[]
dange_num=1
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            dq=deque([(j,i)])
            num=1
            dange_num+=1
            graph[i][j]=dange_num
            while dq:
                x,y=dq.popleft()
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if 0<=nx<N and 0<=ny<N and graph[ny][nx]==1:
                        graph[ny][nx]=dange_num
                        dq.append((nx,ny))
                        num+=1
            dange.append(num)
print(len(dange),*sorted(dange),sep='\n')