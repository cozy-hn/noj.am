N=int(input())

def LIS_nlogn(arr):
    lis=[-10**9-1]
    dp=[0]*(N)
    idx=0
    for i in arr:
        if lis[-1]<i[1]:
            lis.append(i[1])
            dp[idx]=len(lis)-1
        else:
            start,end=0,len(lis)-1
            while start<=end:
                mid=(start+end)//2
                if lis[mid]<i[1]:
                    start=mid+1
                else:
                    end=mid-1
            lis[start]=i[1]
            dp[idx]=start
        idx+=1
    MAX=len(lis)-1
    print(N-MAX)
    maxidx=dp.index(MAX)
    li=[arr[maxidx]]
    for i in range(maxidx-1,-1,-1):
        if arr[i][1]<arr[maxidx][1] and dp[i]==MAX-1:
            li.append(arr[i])
            MAX-=1
            if MAX==1:
                tmp=list(SET-{i[0] for i in li})
                tmp.sort()
                print(*tmp,sep="\n")
                break


li=[tuple(map(int,input().split())) for i in range(N)]
li.sort(key=lambda x:x[0])
SET={i[0] for i in li}
LIS_nlogn(li)