N=int(input())
wine=[int(input()) for _ in range(N)]
dp=[0]*N
dp[0]=wine[0]
for i in range(1,N):
    if i==1:
        dp[i]=dp[i-1]+wine[i]
    elif i==2:
        dp[i]=max(dp[i-2]+wine[i],dp[i-1],wine[i-1]+wine[i])
    else:
        dp[i]=max(dp[i-3]+wine[i-1]+wine[i],dp[i-2]+wine[i],dp[i-1])
print(dp[-1])