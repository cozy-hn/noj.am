N,M=map(int,input().split())
byte=list(map(int,input().split()))
cost=list(map(int,input().split()))

def Knapsack(N,K,byte,cost):
    SUM=sum(cost)
    dp=[[0]*(M+1) for _ in range(2)]
    for i in range(1,N+1):
        for j in range(SUM+1):
            dp[0][j]=dp[1][j]
        for j in range(SUM+1):
            if cost[i-1]<=j:
                dp[1][j]=max(dp[0][j],dp[0][j-cost[i-1]]+byte[i-1])
            else:
                dp[1][j]=dp[0][j]
    for i in range(SUM+1):
        if dp[1][i]>=K:
            return i

print(Knapsack(N,M,byte,cost))
