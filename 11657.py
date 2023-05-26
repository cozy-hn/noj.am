N,M = map(int,input().split())

def BellmanFord(graph, start):
    distance = [INF] * (N+1)
    distance[start] = 0
    for i in range(1,N+1):
        for V in range(1,N+1):
            for E, weight in graph[V]:
                if weight != INF:
                    D=weight+distance[V]
                    if D<distance[E]:
                        distance[E]=D
                        if i==N and distance[E]!=INF:
                            print(-1)
                            exit()
    for i in range(2,N+1):
        if distance[i]==INF:
            print(-1)
        else:
            print(distance[i])

INF=float('inf')
city=[[] for i in range(N+1)]
for _ in range(M):
    S,E,T=map(int,input().split())
    city[S].append((E,T))
BellmanFord(city,1) 