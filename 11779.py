from heapq import heappush, heappop

def Dijkstra(graph, start, end, num_V):
    visited = [False] * (num_V+1)
    distance = [INF] * (num_V+1)
    path={}
    for i in range(1,num_V+1):
        if graph[start][i]!=INF:
            path[i]=start
        else:
            path[i]=None
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
                    path[V]=current_node
                    heappush(heap,(D,V))
    print(distance[end])
    pathlist=[]
    while True:
        pathlist.append(end)
        if end==start:
            break
        end=path[end]
    print(len(pathlist))
    print(*pathlist[::-1])    
    
    

V=int(input())
E=int(input())
INF=float('inf')
city=[[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a,b,c=map(int,input().split())
    city[a][b]=min(city[a][b],c)
start,end=map(int,input().split())
Dijkstra(city,start,end,V)