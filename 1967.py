import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
graph=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

visited=[False]*(N+1)
cost=[0]*(N+1)

def bfs(idx):
    visited[idx]=True
    ans=0
    dq=deque([idx])
    while dq:
        now=dq.popleft()
        for nxt,c in graph[now]:
            if not visited[nxt]:
                visited[nxt]=True
                cost[nxt]=cost[now]+c
                dq.append(nxt)
                if len(graph[nxt])==1:
                    ans=max(ans,cost[nxt])
    return ans

for i in range(1,N+1):
    if len(graph[i])==1:
        idx=i
        break
print(idx)
print(bfs(idx))