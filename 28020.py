import sys
input=sys.stdin.readline

def prefix_sum(i,j):
    result=0
    while i>0:
        result+=tree[i][j]
        i-=(i&-i)
    return result

def update(i,diff,j):
    while i<=n:
        tree[i][j]+=diff
        i+=(i&-i)

n=int(input())
tree=[[0,0] for _ in range(n+1)]
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
weight={}
for i in range(n):
    weight[li1[i]]=i+1
wlist=[weight[li2[i]] for i in range(n)]
ans=[0]*(n+1)
ansrev=[0]*(n+1)
for i in range(n):
    ans[i+1]=prefix_sum(wlist[i],0)
    update(wlist[i],1,0)
    ansrev[n-i]=prefix_sum(n+1-wlist[n-i-1],1)
    update(n+1-wlist[n-i-1],1,1)
rtn=0
for i in range(n):
    rtn+=ans[i+1]*ansrev[i+1]
if rtn==0:
    print("Attention is what I want")
else:
    print("My heart has gone to paradise")
    print(rtn)