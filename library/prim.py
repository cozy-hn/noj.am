# 프림 알고리즘
 
INF = float('inf')
 
# 각 정점 사이의 가중치가 주어진다.
weight = [[0,   7,   INF, INF, 3,  10,   INF],
          [7,   0,   4,   10,  2,   6,   INF],
          [INF, 4,   0,   2,   INF, INF, INF],
          [INF, 10,  2,   0,   INF, 9,   4],
          [3,   2,   INF, INF, 0,   INF, 5],
          [10,  6,   INF, 9,   INF, 0,   INF],
          [INF, INF, INF, 4,   5,   INF, 0]]
 
def prim(weight):
    V_NUM = len(weight)
    dist = [INF for _ in range(V_NUM)]  # 모든 정점에 대해서 집합 S와의 최단거리. 처음에는 모두 무한대라고 가정한다.
    selected = [False for _ in range(V_NUM)]
    dist[0] = 0  # 시작 정점을 선택하고 S에 포함하고, 거리가 0이라고 가정한다. (프림 알고리즘의 시작)
    mst=[0]*V_NUM
    for i in range(V_NUM):  # 정점의 갯수만큼 반복
    
        unselected = [idx for idx, val in enumerate(selected) if not val]
        u = min(unselected, key=lambda x: dist[x])
        # u=아직 집합 S에 포함되지 않은 정점 중에서 집합에 연결되기 위해 최소 비용이 드는 점을 구한다.
    
        selected[u] = True
        mst[i]=u  # S에 포함된 점
    
        for v in range(V_NUM):
            if weight[u][v] != INF:  # u와 연결된 정점 중에서
                if not selected[v] and weight[u][v] < dist[v]:
                    # S에 포함되지 않은 정점 중에서,
                    # 이미 알려진 길(dist[v])보다 더 가까운 길로 갈 수 있으면(weight[u][v]) 갱신한다. 다음에 방문하기 위해서..
                    dist[v] = weight[u][v]
    return mst

print(prim(weight))