import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
graph=[[] for _ in range(N+1)]
for i in range(N):
    ip=[*map(int,input().split())]
    a=ip[0]
    ip=ip[1:-1]
    for i in range(len(ip)//2):
        b,c=ip[2*i],ip[2*i+1]
        graph[a].append((b,c))


def bfs(idx):
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

_,node=bfs(1)
rtn,_=bfs(node)
print(rtn)