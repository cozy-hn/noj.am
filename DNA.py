import sys

input = lambda: sys.stdin.readline().strip()
N,M = map(int, input().split())
DNA = [input() for _ in range(N)]
dist=0
result=""
for i in range(M):
	dict = {'A':0, 'C':0, 'G':0, 'T':0}
	for j in range(N):
		dict[DNA[j][i]]+=1
	max_value = max(dict.values())
	dist += N-max_value
	for key in sorted(dict.keys()):
		if dict[key] == max_value:
			result+=key
			break
print(result)
print(dist)