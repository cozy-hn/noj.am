import sys
input=lambda:sys.stdin.readline().rstrip()
N=int(input())
mtx=[list(map(int, input().split())) for _ in range(N)]
for k in range(N):
  for y in range(N):
    for x in range(N):
      if mtx[y][k]+mtx[k][x]==2:
        mtx[y][x]=1
for i in mtx:
  print(*i)