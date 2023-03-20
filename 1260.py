import sys
from collections import deque

def bfs(V):
    dq=deque([V])
    visited=[]
    while dq:
        out=dq.popleft()
        if out not in visited:
            visited.append(out)
            dq.extend(graph[out])
    print(*visited)

def dfs(V):
    st=[V]
    visited=[]
    while st:
        out=st.pop()
        if out not in visited:
            visited.append(out)
            st.extend(graph[out])
    print(*visited)
    
N,M,V=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)
for i in graph:
    i.sort(reverse=True)
dfs(V)
for i in graph:
    i.sort()
bfs(V)

