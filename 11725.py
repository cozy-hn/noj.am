import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
graph=[set() for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
for i in range(len(graph)):
    graph[i]=list(graph[i])
parent={i:0 for i in range(1,N+1)}
parent[1]=1
dq=deque([1])
while dq:
    node=dq.popleft()
    for i in graph[node]:
        if parent[i]==0:
            parent[i]=node
            dq.append(i)

for i in range(2,N+1):
    print(parent[i])