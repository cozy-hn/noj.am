N=int(input())
dp=[0]+[*map(int,input().split())]
for i in range(1,N+1):
    if dp[i-1]>0:
        dp[i]+=dp[i-1]
print(max(dp[1:]))