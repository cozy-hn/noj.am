import sys
input=sys.stdin.readline
# sys.setrecursionlimit(10**5)

def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

N=int(input())
airport=[False]*(N+1)
ans=0
parent=[i for i in range(N+1)]
for i in range(int(input())):
    plane=int(input())
    if not airport[plane]:
        airport[plane]=True
        union(plane,plane-1)
        ans+=1
    else:
        put=find(plane)
        if put:
            union(plane,put-1)
            airport[put]=True
            ans+=1
        else:
            break
print(ans)