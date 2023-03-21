import sys
from collections import deque

N,M=map(int,input().split())
li=[]
for _ in range(N):
    li.append(list(map(int,sys.stdin.readline().rstrip())))
dq=deque([[0,0]])
dx=[1,0,-1,0]
dy=[0,1,0,-1]
while dq:
    out=dq.popleft()
    for i in range(4):
        nx=out[0]+dx[i]
        ny=out[1]+dy[i]
        if (nx>=0 and nx<= M-1) and (ny>=0 and ny<= N-1) and li[ny][nx] ==1:
            li[ny][nx]=li[out[1]][out[0]]+1
            dq.append([nx,ny])
print(li[N-1][M-1])