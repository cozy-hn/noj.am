import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    time=[0]+list(map(int,input().split()))
    build=[0]*(N+1)
    for i in range(K):
        a,b=map(int,input().split())
        graph[b].append(a)
    dq=deque([int(input())])
    build[dq[0]]=time[dq[0]]
    ans=build[dq[0]]
    while dq:
        now=dq.popleft()
        for i in graph[now]:
            if build[i]<build[now]+time[i]:
                build[i]=build[now]+time[i]
                ans=max(ans,build[i])
                dq.append(i)
    print(ans)