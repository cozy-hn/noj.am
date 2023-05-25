N=int(input())
Map=[[*map(int,input().split())] for _ in range(N)]
row=[[0]*(N+1) for i in range(N+1)]
col=[[0]*(N+1) for i in range(N+1)]
side=[[0]*(N+1) for i in range(N+1)]
row[1][2]=1
for i in range(1,N+1):
    for j in range(1,N+1):
        if Map[i-1][j-1]==1:
            continue
        row[i][j]+=(row[i][j-1]+side[i][j-1])
        col[i][j]+=(col[i-1][j]+side[i-1][j])
        if Map[i-2][j-1]!=1 and Map[i-1][j-2]!=1:
            side[i][j]+=(col[i-1][j-1]+row[i-1][j-1]+side[i-1][j-1])
print(col[N][N]+row[N][N]+side[N][N])