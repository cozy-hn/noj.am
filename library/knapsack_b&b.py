# from collections import deque
from heapq import heappush, heappop

class Item:
    def __init__(self, w, val):
        self.w = w
        self.val = val

class Node:
    def __init__(self, lv, pf, bnd, w):
        self.lv = lv
        self.pf = pf
        self.bnd = bnd
        self.w = w
    
    def __lt__(self, other):
        return self.bnd > other.bnd

def bound(u, n, K, arr):
    if u.w >= K:
        return 0
    profit_B = u.pf
    j = u.lv + 1
    tot_W = u.w
    while j < n and tot_W + arr[j].w <= K:
        tot_W += arr[j].w
        profit_B += arr[j].val
        j += 1
    if j < n:
        profit_B += (K - tot_W) * arr[j].val / arr[j].w
    return profit_B

def knapsack(K, arr, n):
    # q = deque()
    pq=[]
    u = Node(-1, 0, 0, 0)
    # q.append(u)
    heappush(pq, u)
    Max_p = 0
    # while q:
    while pq:
        # u = q.popleft()
        u=heappop(pq)
        if u.bnd < Max_p:
            continue
        if u.lv == n - 1:
            continue
        v = Node(u.lv + 1, u.pf + arr[u.lv + 1].val, 0, u.w + arr[u.lv + 1].w)
        if v.w <= K and v.pf > Max_p:
            Max_p = v.pf
        v.bnd = bound(v, n, K, arr)
        if v.bnd > Max_p:
            # q.append(v)
            heappush(pq, v)
        v = Node(u.lv + 1, u.pf, 0, u.w)
        v.bnd = bound(v, n, K, arr)
        if v.bnd > Max_p:
            # q.append(v)
            heappush(pq, v)
    return Max_p

N, K = map(int, input().split())
items = [Item(*map(int, input().split())) for _ in range(N)]
items.sort(key=lambda x : x.val / x.w, reverse=True)
print (knapsack(K, items, N))