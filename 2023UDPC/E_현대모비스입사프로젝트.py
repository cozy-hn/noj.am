import sys
input=lambda:sys.stdin.readline().rstrip()
N,K=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
li2=li[:]
li3=li[:]
li.sort(key=lambda x : (-x[0]-x[1]))
li2.sort(key=lambda x : (-x[0]-x[2]))
li3.sort(key=lambda x : (-x[1]-x[2]))
ans1=0
for i in range(K):
    ans1+=(li[i][0]+li[i][1])
ans2=0
for i in range(K):
    ans2+=(li2[i][0]+li2[i][2])
ans3=0
for i in range(K):
    ans3+=(li3[i][1]+li3[i][2])
print(max(ans1,ans2,ans3))