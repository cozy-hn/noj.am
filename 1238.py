import sys
from heapq import heappush, heappop
input=sys.stdin.readline
N,M,X=map(int,input().split())
INF=10**7

def Dijkstra(graph, start, num_V):
    visited = [False] * (num_V+1)
    distance = [INF] * (num_V+1)
    distance[start], visited[start] = 0, True
    heap=[(0,start)]
    while heap:
        current_distance, current_node = heappop(heap)
        visited[current_node] = True
        for V, weight in enumerate(graph[current_node]):
            if weight != INF and visited[V] == False:
                D=weight+current_distance
                if D<distance[V]:
                    distance[V]=D
                    heappush(heap,(D,V))
    return distance

graph=[[INF]*(N+1) for _ in range(N+1)]
revgraph=[[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i]=0
    revgraph[i][i]=0

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a][b]=min(graph[a][b],c)
    revgraph[b][a]=min(revgraph[b][a],c)


ans=[0]*N
go=Dijkstra(graph,X,N)
home=Dijkstra(revgraph,X,N)
for i in range(1,N+1):
    ans[i-1]=go[i]+home[i]
print(max(ans))