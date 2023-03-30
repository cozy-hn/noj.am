from collections import deque
A,B=map(int,input().split())
visit_dic={}
dq=deque([A])
visit_dic[A]=1
while dq:
    x=dq.popleft()
    for i in range(2):
        if i==0:
            tx=2*x
        else:
            tx=10*x+1
        if 1<=tx<=B and visit_dic.get(tx,0)==0:
            visit_dic[tx]=visit_dic[x]+1
            dq.append(tx)
        if tx==B:
            print(visit_dic[tx])
            exit(0)
print(-1)