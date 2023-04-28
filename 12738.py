N=int(input())

def LIS_nlogn(arr):
    lis=[-10**9-1]
    for i in arr:
        # print("lis:",lis)
        if lis[-1]<i:
            lis.append(i)
            # print("lis[-1]:",lis[-1])
        else:
            start,end=0,len(lis)-1
            while start<=end:
                mid=(start+end)//2
                # print("mid:",mid)
                # print("lis[mid]:",lis[mid])
                if lis[mid]<i:
                    start=mid+1
                else:
                    end=mid-1
            lis[start]=i
    return len(lis)-1

ip=[*map(int,input().split())]
print(LIS_nlogn(ip))