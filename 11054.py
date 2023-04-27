N=int(input())

def LIS(arr):
    dp=[1]*N
    dp2=[1]*N
    arr2=arr[::-1]
    for i in range(N):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    for i in range(N):
        for j in range(i):
            if arr2[i]>arr2[j]:
                dp2[i]=max(dp2[i],dp2[j]+1)
    dp2=dp2[::-1]
    return max(dp[i]+dp2[i] for i in range(N))-1

print(LIS(list(map(int,input().split()))))