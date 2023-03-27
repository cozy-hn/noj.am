import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
visit=[0]*(N+1)
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=0
for i in range(1,N+1):
    if visit[i]==0:
        visit[i]=1
        dq=deque()
        dq.append(i)
        cnt+=1
        while dq:
            o=dq.popleft()
            for j in graph[o]:
                if visit[j]==0:
                    visit[j]=1
                    dq.append(j)
print(cnt)