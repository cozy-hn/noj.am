li=list(map(int,[*open(0)]))
dp=[0]*(li[0]+1)
dp[1]=li[1]
if li[0]>1:
    dp[2]=li[1]+li[2]
for i in range(3,li[0]+1):
    dp[i]=max(dp[i-3]+li[i-1],dp[i-2])+li[i]
print(dp[-1])