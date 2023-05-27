from itertools import combinations
N,M= map(int, input().split())
Map=[[*map(int, input().split())] for _ in range(N)]
chicken={}
house={}
for i in range(N):
    for j in range(N):
        if Map[i][j]==2:
            chicken[(i,j)]=0
        if Map[i][j]==1:
            house[(i,j)]=0
Clist=list(chicken.keys())
Hlist=list(house.keys())

def distance(home, list_):
    ans=100000000
    for i in range(len(list_)):
        ans=min(ans, abs(home[0]-list_[i][0])+abs(home[1]-list_[i][1]))
    house[home]=ans
    return ans

tmp=100000000
def dfs():
    global tmp
    for i in combinations(Clist, M):
        ttmp=0
        for j in range(len(Hlist)):
            ttmp+=distance(Hlist[j], i)
            if ttmp>tmp:
                break
        tmp=min(tmp, ttmp)
dfs()
print(tmp)