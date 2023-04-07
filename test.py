import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
N=int(input())
Map=[list(map(int,input().split())) for _ in range(N)]
size=2
eat=0
dq=deque()
for i in range(N):
	for j in range(N):
		if Map[i][j]==9:
			Map[i][j]=0
			dq.append((i,j,0))
			break