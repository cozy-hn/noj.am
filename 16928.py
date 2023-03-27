import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
def bfs():
    graph=[0]*101
    dq=deque([1])
    dx=[1,2,3,4,5,6]
    while dq:
        x=dq.popleft()
        if x==100:
            break
        for i in dx:
            dn=x+i
            if 1<dn<=100 and graph[dn]==0:
                graph[dn]=graph[x]+1
                for j in shortcut:
                    if dn==j[0]:
                        dn=j[1]
                        if graph[dn]==0:
                            graph[dn]=graph[x]+1
                            dq.append(dn)
                        break
                else:
                    dq.append(dn)
    print(graph[100])
    
shortcut=[]
for _ in range(sum(map(int,input().split()))):
    shortcut.append(tuple(map(int,input().split())))
bfs()