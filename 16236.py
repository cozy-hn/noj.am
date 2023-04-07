import sys
from collections import deque
input=lambda: sys.stdin.readline().rstrip()

def check():
    global size
    for i in range(N):
        for j in range(N):
            if li[i][j]!=0 and li[i][j]<size:
                return True
    return False

N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]
dq=deque()
size=2
eat=0
for i in range(N):
    for j in range(N):
        if li[i][j]==9:
            li[i][j]=0
            dq.append((j,i,0))
            break

dx=[0,-1,1,0]
dy=[-1,0,0,1]
if not check():
    print(0)
    exit()
flag=False
tmp=0
while dq:
    x,y,cnt=dq.popleft()
    visited[y][x]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and li[ny][nx]<=size and not visited[ny][nx]:
            dq.append((nx,ny,cnt+1))
            visited[ny][nx]=True
            if li[ny][nx]<size and li[ny][nx]!=0:
                flag=True
    if flag and cnt!=dq[0][2]:
        dq = deque(sorted(dq, key=lambda x: (x[1], x[0])))
        while li[dq[0][1]][dq[0][0]]==0 or li[dq[0][1]][dq[0][0]]==size:
            dq.popleft()
        dq=deque([dq[0]])
        tmp=dq[0][2]
        eat+=1
        if eat==size:
            eat=0
            size+=1
        flag=False
        li[dq[0][1]][dq[0][0]]=0
        visited=[[False]*N for _ in range(N)]
        if not check():
            break
print(tmp)
