import sys

input = sys.stdin.readline

def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        parent[y]=x

def kruscal(graph):
    global MAX
    mst,line=0,0
    for a,b,c in graph:
        if find(a)!=find(b):
            MAX=max(MAX,c)
            union(a,b)
            mst+=c
            line+=1
            if line == V-1:
                break
    return mst-MAX

MAX=1
V,E=map(int,input().split())
graph=[tuple(map(int,input().split())) for _ in range(E)]
parent=[i for i in range(V+1)]
graph.sort(key=lambda x:x[2])
print(kruscal(graph))