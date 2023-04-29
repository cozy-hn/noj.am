from heapq import heappush, heappop

def Dijkstra(graph, start, end, num_V):
    visited = [False] * (num_V+1)
    distance = [INF] * (num_V+1)
    distance[start], visited[start] = 0, True
    heap=[(0,start)]
    while visited[end] == False:
        current_distance, current_node = heappop(heap)
        visited[current_node] = True
        for V, weight in enumerate(graph[current_node]):
            if weight != INF and visited[V] == False:
                D=weight+current_distance
                if D<distance[V]:
                    distance[V]=D
                    heappush(heap,(D,V))
    return distance[end]
    

V=int(input())
E=int(input())
INF=float('inf')
city=[[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a,b,c=map(int,input().split())
    city[a][b]=min(city[a][b],c)
start,end=map(int,input().split())
print(Dijkstra(city,start,end,V))