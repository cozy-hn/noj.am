N=int(input())
MOD=10**9
dp=[[[0]*1024 for _ in range(10)] for _ in range(N+1)]
for i in range(1,10):
    dp[1][i][1<<i]=1

for i in range(2,N+1):
    for j in range(10):
        for k in range(1024):
            if j!=9 and j!=0:
                dp[i][j][k|(1<<j)]+=dp[i-1][j-1][k]+dp[i-1][j+1][k]%MOD
            elif j==0:
                dp[i][j][k|(1<<j)]+=dp[i-1][j+1][k]%MOD
            else:
                dp[i][j][k|(1<<j)]+=dp[i-1][j-1][k]%MOD

print(sum(dp[N][i][1023] for i in range(10))%MOD)