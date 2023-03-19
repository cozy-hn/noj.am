import sys

M, N, B = map(int, sys.stdin.readline().split())
ground=[]
for _ in range(M):
	ground.append(list(map(int, sys.stdin.readline().split())))
m = min(map(min, ground))
ma = max(map(max, ground))
ans=[]
while True:
	inv = B
	time = 0
	for row in ground:
		for i in row:
			if i > m:
				time += ((i-m) * 2)
				inv += (i-m)
	for row in ground:
		for i in row:
			if i < m:
				time += (m-i)
				inv -= (m-i)
	if inv >= 0:
		ans.append((time,m))
	m+=1
	if m > ma:
		break
ans.sort(key = lambda x: (x[0],-x[1]))
print(*ans[0])