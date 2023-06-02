import sys
input = sys.stdin.readline
N=int(input())
point=[tuple(map(int,input().split())) for _ in range(N)]
point.append(point[0])
ans=0
for i in range(N):
    ans+=((point[i][0]+point[i+1][0])*(point[i][1]-point[i+1][1]))
print(abs(ans)/2)