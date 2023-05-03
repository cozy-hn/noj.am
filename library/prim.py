INF = float('inf')
weight = [[0,   7,   INF, INF, 3,  10,   INF],
          [7,   0,   4,   10,  2,   6,   INF],
          [INF, 4,   0,   2,   INF, INF, INF],
          [INF, 10,  2,   0,   INF, 9,   4],
          [3,   2,   INF, INF, 0,   INF, 5],
          [10,  6,   INF, 9,   INF, 0,   INF],
          [INF, INF, INF, 4,   5,   INF, 0]]
 
def prim(weight):
    V_NUM = len(weight)
    dist = [INF for _ in range(V_NUM)]  
    selected = [False for _ in range(V_NUM)]
    dist[0] = 0  
    mst=0
    for i in range(V_NUM):  
        unselected = [idx for idx, val in enumerate(selected) if not val]
        u = min(unselected, key=lambda x: dist[x])
        selected[u] = True 
        mst+=dist[u]
    
        for v in range(V_NUM):
            if weight[u][v] != INF:
                if not selected[v] and weight[u][v] < dist[v]:
                    dist[v] = weight[u][v]
    return mst

print(prim(weight))