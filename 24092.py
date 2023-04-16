import sys
sys.setrecursionlimit(int(1e4))

N=int(input())
Set=set()
ip=list(map(int,input().split()))
ip2=list(map(int,input().split()))

for i in range(N):
    if ip[i]!=ip2[i]:
        Set.add(i)

def issame(idx,arr,findarr):
    if idx in Set:
        if arr[idx]==findarr[idx]:
            Set.remove(idx)
    elif arr[idx]!=findarr[idx]:
        Set.add(idx)
    if not Set:
        print(1)
        exit()

def partition(arr,left,right,findarr):
    pivot=arr[right]
    i=left-1
    for j in range(left,right):
        if arr[j]<=pivot:
            i+=1
            if i != j:
                arr[i],arr[j]=arr[j],arr[i]
                issame(i,arr,findarr)
                issame(j,arr,findarr)
    if i+1 != right:
        arr[i+1],arr[right]=arr[right],arr[i+1]
        issame(i+1,arr,findarr)
        issame(right,arr,findarr)

    return i+1 
    
def Quick_sort(arr,left,right,findarr):
    if left<right:
        pi=partition(arr,left,right,findarr)
        Quick_sort(arr,left,pi-1,findarr)
        Quick_sort(arr,pi+1,right,findarr)

if not Set:
    print(1)
else:
    Quick_sort(ip,0,N-1,ip2)
    print(0)