from collections import deque
N,M=map(int,input().split())
dq=deque([i for i in range(1,N+1)])
get=list(map(int,input().split()))
ans=0
for i in get:
    idx=dq.index(i)
    if idx<=len(dq)-idx-1:
        while dq[0]!=i:
            dq.append(dq.popleft())
            ans+=1
        dq.popleft()
    else:
        while dq[0]!=i:
            dq.appendleft(dq.pop())
            ans+=1
        dq.popleft()
print(ans)
