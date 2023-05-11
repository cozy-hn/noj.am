from collections import deque
N,M=map(int,input().split())
Map=[list(map(int,input().split())) for _ in range(N)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
vir=[]
zero=[]

def findvir():
    for i in range(N):
        for j in range(M):
            if Map[i][j]==2:
                vir.append((j,i)) # x,y

def findzero():
    for i in range(N):
        for j in range(M):
            if Map[i][j]==0:
                zero.append((j,i))

def bfs(MAP):
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<M and 0<=ny<N and MAP[ny][nx]==0:
                MAP[ny][nx]=2
                dq.append((nx,ny))
    count=sum(i.count(0) for i in MAP)
    return count

ret=0
findvir()
findzero()
lenzero=len(zero)
for i in range(lenzero):
    for j in range(i+1,lenzero):
        for k in range(j+1,lenzero):
            MAP=[i[:] for i in Map]
            MAP[zero[i][1]][zero[i][0]]=1
            MAP[zero[j][1]][zero[j][0]]=1
            MAP[zero[k][1]][zero[k][0]]=1
            dq=deque(vir)
            ret=max(ret,bfs(MAP))
print(ret)
            