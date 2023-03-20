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
        if (out[0]+dx[i] >=0 and out[0]+dx[i] <= M-1) and (out[1]+dy[i] >=0 and out[1]+dy[i] <= N-1):
            if li[out[1]+dy[i]][out[0]+dx[i]]==1:
                li[out[1]+dy[i]][out[0]+dx[i]]=li[out[1]][out[0]]+1
                dq.append([out[0]+dx[i],out[1]+dy[i]])
            elif li[out[1]+dy[i]][out[0]+dx[i]] >1:
                li[out[1]+dy[i]][out[0]+dx[i]]=min(li[out[1]][out[0]]+1,li[out[1]+dy[i]][out[0]+dx[i]])
                if li[out[1]][out[0]]+1 < li[out[1]+dy[i]][out[0]+dx[i]]:
                    dq.append([out[0]+dx[i], out[1]+dy[i]])
print(li[N-1][M-1])