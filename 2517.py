import sys
input=sys.stdin.readline

def prefix_sum(i):
    result=0
    while i>0:
        result+=tree[i]
        i-=(i&-i)
    return result

def update(i,diff):
    while i<=n:
        tree[i]+=diff
        i+=(i&-i)

n=int(input())
tree=[0]*(n+1)
li=list(int(input()) for _ in range(n))
rcp=list(reversed(sorted(li)))
weight={}
for i in range(n):
    weight[rcp[i]]=i+1
ans=[0]*(n+1)
for i in range(n):
    ans[i+1]=prefix_sum(weight[li[i]])+1
    update(weight[li[i]],1)
print(*ans[1:],sep='\n')