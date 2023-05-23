import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

graph=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def bfs1(idx):
    cost=[0]*(N+1)
    visited=[False]*(N+1)
    visited[idx]=True
    ans=0
    dq=deque([idx])
    node=idx
    while dq:
        now=dq.popleft()
        for nxt,c in graph[now]:
            if not visited[nxt]:
                visited[nxt]=True
                cost[nxt]=cost[now]+c
                dq.append(nxt)
                if len(graph[nxt])==1:
                    if cost[nxt]>=ans:
                        ans=cost[nxt]
                        node=nxt
    return ans, node

def bfs2(idx):
    cost=[0]*(N+1)
    visited=[False]*(N+1)
    visited[idx]=True
    ans=0
    dq=deque([idx])
    node=idx
    while dq:
        now=dq.popleft()
        for nxt,c in graph[now]:
            if not visited[nxt]:
                visited[nxt]=True
                cost[nxt]=cost[now]+c
                dq.append(nxt)
                if len(graph[nxt])==1:
                    if cost[nxt]>=ans:
                        ans=cost[nxt]
                        node=nxt
    cost.sort()
    return cost[-2], node

_,node1=bfs1(1)
N1,node2=bfs2(node1)
N2,_=bfs2(node2)
print(max(N1,N2))
