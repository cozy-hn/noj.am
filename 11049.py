import sys
input=lambda: sys.stdin.readline().rstrip()

N=int(input())
d=[tuple(map(int,input().split())) for _ in range(N)]
mtx=[[0]*N for _ in range(N)]
for i in range(1,N):
    for j in range(N-i):
        mtx[j][j+i]=min(mtx[j][j+k]+mtx[j+k+1][j+i]+d[j][0]*d[j+k][1]*d[j+i][1] for k in range(i))
print(mtx[0][N-1])