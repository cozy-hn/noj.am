import sys
import math

input=lambda: sys.stdin.readline()

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

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

V=int(input())
points=[tuple(map(float,input().split())) for _ in range(V)]
graph=[]
for i in range(V):
    for j in range(i+1,V):
        graph.append((i+1,j+1,distance(points[i],points[j])))
parent=[i for i in range(V+1)]
graph.sort(key=lambda x:x[2])
print(kruscal(graph))