from collections import deque
N,K=map(int,input().split())
graph=[0]*100001
graph[N]=0
dq=deque([(N,0)])
if N>=K:
    print(N-K)
    dq=deque()
while dq:
    o=dq.popleft()
    if N>K:
        li=[o[0]-1]
    else:
        li=[o[0]-1,o[0]+1,o[0]*2]
    for i in li:
        if i==K:
          print(o[1]+1)
          dq=deque()
          break 
        if 0<=i<=100000 and graph[i]==0:
            dq.append((i,o[1]+1))
            graph[i]=1