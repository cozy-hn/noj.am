import sys

input = lambda: sys.stdin.readline().rstrip()

N,M,K = map(int,input().split())
MAP=[list(input()) for _ in range(N)]
prefix1 = [[0]*(M+1) for _ in range(N+1)]
prefix2 = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        first,second = 0,0
        if ((i+j)%2==0 and MAP[i][j]=='W') or ((i+j)%2==1 and MAP[i][j]=='B'):
            first += 1
        else:
            second += 1
        prefix1[i+1][j+1] = prefix1[i][j+1]+prefix1[i+1][j]-prefix1[i][j]+first
        prefix2[i+1][j+1] = prefix2[i][j+1]+prefix2[i+1][j]-prefix2[i][j]+second

MIN=K**2

for i in range(K,N+1):
	for j in range(K,M+1):
		MIN = min(MIN,prefix1[i][j]-prefix1[i-K][j]-prefix1[i][j-K]+prefix1[i-K][j-K],prefix2[i][j]-prefix2[i-K][j]-prefix2[i][j-K]+prefix2[i-K][j-K])

print(MIN)