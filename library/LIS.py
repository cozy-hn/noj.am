def LIS_nlogn(arr):
    lis=[0]
    for i in arr:
        if lis[-1]<i:
            lis.append(i)
        else:
            start,end=0,len(lis)-1
            while start<=end:
                mid=(start+end)//2
                if lis[mid]<i:
                    start=mid+1
                else:
                    end=mid-1
            lis[start]=i
    return len(lis)-1