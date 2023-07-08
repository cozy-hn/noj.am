N=int(input())
arr=list(map(int,input().split()))
arr.sort()

def two_pointer(arr):
    MIN=3*10**9
    for i in range(N-2):
        left,right=i+1,N-1
        while left<right:
            sol=arr[i]+arr[left]+arr[right]
            if abs(sol)<MIN:
                MIN=abs(sol)
                ret=[arr[i],arr[left],arr[right]]
            if sol<0:
                left+=1
            else:
                right-=1
    return ret

print(*two_pointer(arr))