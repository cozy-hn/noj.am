import sys
input = sys.stdin.readline

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
                        if i==N:
                            return True
    return False

    
INF=10**9
for _ in range(int(input())):
    N,M,W=map(int,input().split())
    city=[[] for i in range(N+1)]
    for _ in range(M):
        S,E,T=map(int,input().split())
        city[S].append((E,T))
        city[E].append((S,T))
    for i in range(W):
        S,E,T=map(int,input().split())
        city[S].append((E,-T))
    if BellmanFord(city,1):
        print('YES')
    else:
        print('NO')
