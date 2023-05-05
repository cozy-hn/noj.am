def Knapsack(N,K,item): # item: [(weight,value),...]
    dp=[[0]*(K+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,K+1):
            if item[i-1][0]<=j:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-item[i-1][0]]+item[i-1][1])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[N][K]