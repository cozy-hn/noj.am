import sys

input= sys.stdin.readline
sys.setrecursionlimit(10**6)

li=list(input().rstrip())
N=len(li)
dp=[[-1]*(N+1) for _ in range(N+1)]

def solve(i,j):
    if i==j:
        dp[i][j]=1
        return 1
    if i+1==j:
        if li[i-1]==li[j-1]:
            dp[i][j]=1
            return 1
        else:
            dp[i][j]=0
            return 0
    if dp[i][j]==-1:
        if solve(i+1,j-1) and li[i-1]==li[j-1]:
            dp[i][j]=1
            return 1
        else:
            dp[i][j]=0
            return 0
    else:
        return dp[i][j]
    

dp2=[0]*(N+1)
for i in range(1,N+1):
    for j in range(i,N+1):
        if solve(i,j):
            dp2[j]=min(dp2[j],dp2[i-1]+1) if dp2[j] else dp2[i-1]+1
print(dp2[-1])