import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    cyc=0
    lst=[0]+[*map(int,input().split())]
    visited=[0]*(N+1)
    path=[0]*(N+1)
    dq=deque()
    for i in range(1,N+1):
        if visited[i]==0:
            cnt=1
            path[i]=cnt
            dq.append(lst[i])
            while dq:
                now=dq.popleft()
                if visited[now]==0:
                    visited[now]=i
                    if lst[now]==now:
                        cyc+=1
                        break
                    if visited[lst[now]]== i and path[lst[now]]!=0:
                        cyc+=cnt-path[lst[now]]+2
                        break
                    cnt+=1
                    path[now]=cnt
                    dq.append(lst[now])
    print(N-cyc)