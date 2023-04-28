def LIS_nlogn(arr):
    lis=[0]
    rtn=0
    plus=0
    for i in arr:
        if lis[-1]<i:
            lis.append(i)
            plus+=1
        else:
            start,end=0,len(lis)-1
            while start<=end:
                mid=(start+end)//2
                if lis[mid]<i:
                    start=mid+1
                else:
                    end=mid-1
            lis[start]=i
        rtn+=plus
    return rtn

for i in range(int(input())):
    ans=0
    li=[int(input()) for _ in range(int(input()))]
    for j in range(len(li)):
        tmp=li[j:]
        ans+=LIS_nlogn(tmp)
    print(f"Case #{i+1}: {ans}")