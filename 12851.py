from collections import deque
N,K=map(int,input().split())
graph=[0]*100001
graph[N]=0
dq=deque([(N,0)])
if N>=K:
    print(N-K)
    print(1)
    dq=deque()
cnt=0
flag=False
while dq:
    o=dq.popleft()
    if N>K:
        li=[o[0]-1]
    else:
        li=[o[0]-1,o[0]+1,o[0]*2]
    for i in li:
        if flag and ans!=o[1]+1:
            print(ans)
            print(cnt)
            dq=deque()
            break
        if i==K:
          ans=o[1]+1
          flag=True
          cnt+=1 
        if 0<=i<=100000 and graph[i]<4:
            dq.append((i,o[1]+1))
            graph[i]+=1