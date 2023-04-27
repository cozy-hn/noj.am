N=int(input())

def LIS(arr):
    dp=[1]*N
    for i in range(N):
        for j in range(i):
            if arr[i][1]>arr[j][1]:
                dp[i]=max(dp[i],dp[j]+1)

    return max(dp)

li=[tuple(map(int,input().split())) for i in range(N)]
li.sort(key=lambda x:x[0])
print(N-LIS(li))