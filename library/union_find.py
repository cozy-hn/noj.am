import sys
sys.setrecursionlimit(10**5)
input=lambda:sys.stdin.readline()
N,M=map(int,input().split())
parent=[i for i in range(N+1)]

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

