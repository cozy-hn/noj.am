N=int(input())

def LIS(arr,K):
    dp=[0]*101
    for i in range(N):
        if arr[i]-K>100 or arr[i]-K<0:
            dp[arr[i]]=1
        else:
            dp[arr[i]]=dp[arr[i]-K]+1
    return max(dp)

li=list(map(int,input().split()))
print(max(LIS(li,i) for i in range(-99,100)))