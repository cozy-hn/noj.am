import sys
input=lambda:sys.stdin.readline().rstrip()
N,M=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
prefix_sum=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            prefix_sum[i][j]=li[i][j]
        elif i==0:
            prefix_sum[i][j]=prefix_sum[i][j-1]+li[i][j]
        elif j==0:
            prefix_sum[i][j]=prefix_sum[i-1][j]+li[i][j]
        else:
            prefix_sum[i][j]=prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+li[i][j]
for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    if x1==0 and y1==0:
        print(prefix_sum[x2][y2])
    elif x1==0:
        print(prefix_sum[x2][y2]-prefix_sum[x2][y1-1])
    elif y1==0:
        print(prefix_sum[x2][y2]-prefix_sum[x1-1][y2])
    else:
        print(prefix_sum[x2][y2]-prefix_sum[x2][y1-1]-prefix_sum[x1-1][y2]+prefix_sum[x1-1][y1-1])
