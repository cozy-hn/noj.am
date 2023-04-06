import sys


input=lambda:sys.stdin.readline()
V,E=map(int,input().split())
startV=int(input())

INF=10**6
graph=[[] for _ in range(V)]

for _ in range(E):
    u,v,w=map(int,input().split())
    # for i in graph[u-1]:
    #     if i[0]==v-1:
    #         i[1]=min(i[1],w)
    #         break
    # else:
    graph[u-1].append([v-1,w])
visited=[False]*V
li=[INF]*V
li[startV-1]=0
while True:
    m=INF
    idx=startV-1
    for i in range(V):
        if not visited[i] and li[i]<m:
            m=li[i]
            idx=i 
    if m==INF:
        break
    else:
        visited[idx]=True
        for i in graph[idx]:
            if not visited[i[0]]:
                li[i[0]]=min(li[i[0]],li[idx]+i[1])
for i in range(V):
    if li[i]==INF:
        print('INF')
    else:
        print(li[i])