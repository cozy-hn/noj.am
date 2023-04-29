N=int(input())
Map=[[0]*(N+1) for _ in range(N+1)]
s1,s2=[*map(int,input().split())],[*map(int,input().split())]
for i in range(1,N+1):
    for j in range(1,N+1):
        Map[i][j]=(s1[i-1]-s2[j-1])**2
dp=[[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    dp[i][1]=dp[i-1][1]+Map[i][1]
    dp[1][i]=dp[1][i-1]+Map[1][i]
for i in range(2,N+1):
    for j in range(2,N+1):
        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+Map[i][j]

print(dp[N][N])
