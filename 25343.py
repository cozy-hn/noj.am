import sys
input=sys.stdin.readline

N=int(input())
List=[list(map(int,input().split())) for _ in range(N)]
dp=[[1 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(i+1):
            for l in range(j+1):
                if List[k][l]<List[i][j]:
                    dp[i][j]=max(dp[i][j],dp[k][l]+1)

print(max(map(max,dp)))