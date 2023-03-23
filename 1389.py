import sys
from collections import deque

def bfs(idx):
    dq=deque([(idx,0)])
    visited=[idx]
    visi_cnt=[0]
    while dq:
        o=dq.popleft()
        for i in graph[o[0]]:
            if i not in visited:
                visited.append(i)
                visi_cnt.append(o[1]+1)
                dq.append((i,o[1]+1))
    return(sum(visi_cnt))
    
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)
li=[bfs(i) for i in range(1,N+1)]
print(li.index(min(li))+1)