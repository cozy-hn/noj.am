N=int(input())

def LIS_nlogn(arr):
    lis=[-10**9-1]
    dp=[0]*(N)
    idx=0
    for i in arr:
        if lis[-1]<i:
            lis.append(i)
            dp[idx]=len(lis)-1
        else:
            start,end=0,len(lis)-1
            while start<=end:
                mid=(start+end)//2
                if lis[mid]<i:
                    start=mid+1
                else:
                    end=mid-1
            lis[start]=i
            dp[idx]=start
        idx+=1
    MAX=len(lis)-1
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

ip=[*map(int,input().split())]
LIS_nlogn(ip)