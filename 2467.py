N=int(input())
li=[*map(int,input().split())]
li.sort()
Min=[0,0,10**11]
zero=0

def BinarySearch(key, start, end):
    global Min, zero
    mid=(start+end)//2
    while start<=end:
        mid=(start+end)//2
        if li[mid]==key:
            Min[0]=li[zero]
            Min[1]=li[mid]
            Min[2]=0
            return
        if li[mid]>key:
            end=mid-1
        else:
            start=mid+1
    if abs(key-li[mid])<Min[2]:
        Min[0]=li[zero]
        Min[1]=li[mid]
        Min[2]=abs(key-li[mid])
    if mid-1!=zero and abs(key-li[mid-1])<Min[2]:
        Min[0]=li[zero]
        Min[1]=li[mid-1]
        Min[2]=abs(key-li[mid-1])
    if mid+1 < N and abs(key-li[mid+1])<Min[2]:
        Min[0]=li[zero]
        Min[1]=li[mid+1]
        Min[2]=abs(key-li[mid+1])

if li[-1]<0:
    print(li[-2],li[-1])
    exit()
if li[0]>0:
    print(li[0],li[1])
    exit()
for i in range(N-1):
    zero=i
    BinarySearch(-li[i],i+1,N-1)
print(Min[0],Min[1])    