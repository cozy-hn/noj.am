import sys
input=sys.stdin.readline

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
    mst,line=0,0
    for a,b,c in graph:
        if find(a)!=find(b):
            union(a,b)
            mst+=c
            line+=1
            if line == V-1:
                break
    return mst

V=int(input())
planet=[(*map(int,input().split()),i) for i in range(V)]
planet.sort(key=lambda x:x[0])
graph=[0]*(3*(V-1))
for i in range(V-1):
    graph[i]=(planet[i][3],planet[i+1][3],planet[i+1][0]-planet[i][0])
planet.sort(key=lambda x:x[1])
for i in range(V-1):
    graph[V-1+i]=(planet[i][3],planet[i+1][3],planet[i+1][1]-planet[i][1])
planet.sort(key=lambda x:x[2])
for i in range(V-1):
    graph[2*(V-1)+i]=(planet[i][3],planet[i+1][3],planet[i+1][2]-planet[i][2])
parent=[i for i in range(V+1)]
graph.sort(key=lambda x:x[2])
print(kruscal(graph))