import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
MOD=10**9+7
arr=[0]*(n+1)
tree=[1]*(n+1)
zerotree=[0]*(n+1)
zero=[False]*(n+1)

def prefix_sum(i):
    result=0
    while i>0:
        result+=zerotree[i]
        i-=(i&-i)
    return result

def sum_update(i,diff):
    while i<=n:
        zerotree[i]+=diff
        i+=(i&-i)

def interval_sum(start,end):
    return prefix_sum(end)-prefix_sum(start-1)

def prefix_mul(i):
    result=1
    while i>0:
        result=(result*tree[i])%MOD
        i-=(i&-i)
    return result

def update(i,diff):
    while i<=n:
        tree[i]=(tree[i]*diff)%MOD
        i+=(i&-i)

def interval_mul(start,end):
    return prefix_mul(end)*pow(prefix_mul(start-1),MOD-2,MOD)%MOD

for i in range(1,n+1):
    x=int(input())
    arr[i]=x
    if x==0:
        update(i,1)
        zero[i]=True
        sum_update(i,1)
    else:
        update(i,x)
    
for i in range(m+k):
    # print(tree)
    a,b,c=map(int,input().split())
    if a==1:
        if zero[b] and c==0:
            continue
        if c==0 and not zero[b]:
            c=1
            sum_update(b,1)
            zero[b]=True
        else:
            if zero[b]:
                sum_update(b,-1)
                zero[b]=False
        update(b,c*pow(arr[b],MOD-2,MOD)%MOD)
        arr[b]=c
        
    else:
        if interval_sum(b,c)!=0:
            print(0)
        else:
            print(interval_mul(b,c))