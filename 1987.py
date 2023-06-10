R,C=map(int,input().split())
Map=[list(input()) for _ in range(R)]
numMap=[[ord(Map[i][j])-65 for j in range(C)] for i in range(R)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
alpha=[False]*26
ans=0

def dfs(x,y,cnt):
    global ans
    ans=max(ans,cnt)
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        suck=0
        if 0<=nx<R and 0<=ny<C and not alpha[numMap[nx][ny]]:
            alpha[numMap[nx][ny]]=True
            dfs(nx,ny,cnt+1)
            alpha[numMap[nx][ny]]=False
        else:
            suck+=1

alpha[numMap[0][0]]=True
dfs(0,0,1)
print(ans)