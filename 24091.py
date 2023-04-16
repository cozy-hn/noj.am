import sys
sys.setrecursionlimit(int(1e4))

N,K=map(int,input().split())
ip=list(map(int,input().split()))
cnt=0
def partition(arr,left,right):
    global cnt
    pivot=arr[right]
    i=left-1
    for j in range(left,right):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            cnt+=1
            if cnt==K:
                print(*ip)
                exit()
    if i+1 != right:
        arr[i+1],arr[right]=arr[right],arr[i+1]
        cnt+=1
        if cnt==K:
            print(*ip)
            exit()
    return i+1 
    
def Quick_sort(arr,left,right):
    if left<right:
        pi=partition(arr,left,right)
        Quick_sort(arr,left,pi-1)
        Quick_sort(arr,pi+1,right)

Quick_sort(ip,0,N-1)
print(-1)