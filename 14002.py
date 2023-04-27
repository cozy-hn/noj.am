N=int(input())

def LIS(arr):
    dp=[1]*N
    for i in range(N):
        # print(dp)
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    MAX=max(dp)
    print(MAX)
    maxidx=dp.index(MAX)
    if MAX==1:
        print(arr[0])
        return
    li=[arr[maxidx]]
    for i in range(maxidx-1,-1,-1):
        if arr[i]<arr[maxidx] and dp[i]==MAX-1:
            li.append(arr[i])
            MAX-=1
            if MAX==1:
                print(*li[::-1])
                break

LIS(list(map(int,input().split())))