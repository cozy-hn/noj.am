from heapq import heappush, heappop
import sys

input=sys.stdin.readline

def Dijkstra(graph, start, end, num_V):
    visited = [False] * (num_V+1)
    distance = [INF] * (num_V+1)
    distance[start], visited[start] = 0, True
    heap=[(0,start)]
    while heap and visited[end] == False:
        current_distance, current_node = heappop(heap)
        visited[current_node] = True
        for V, weight in enumerate(graph[current_node]):
            if weight != INF and visited[V] == False:
                D=weight+current_distance
                if D<distance[V]:
                    distance[V]=D
                    heappush(heap,(D,V))
    if visited[end] == False:
        return -1
    return distance[end]

V, E=map(int,input().split())
if E==0:
    print(-1)
    exit()
INF=float('inf')
city=[[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a,b,c=map(int,input().split())
    city[a][b]=min(city[a][b],c)
    city[b][a]=min(city[b][a],c)
n1,n2=map(int,input().split())
start,end=1,V
D1=Dijkstra(city,start,n1,V)
D2=Dijkstra(city,n1,end,V)
D3=Dijkstra(city,n1,n2,V)
D4=Dijkstra(city,n2,end,V)
D5=Dijkstra(city,start,n2,V)
if D1==-1 or D2==-1 or D3==-1 or D4==-1 or D5==-1:print(-1)
else:print(min(D1+D3+D4,D5+D3+D2))
