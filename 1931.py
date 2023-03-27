import sys
input=lambda:sys.stdin.readline().rstrip()
li=[list(map(int,input().split())) for _ in range(int(input()))]
li.sort(key=lambda x: (-x[0],x[1]))
time=li[0][0]
cnt=1
for i in range(1,len(li)):
    if li[i-1][0]==li[i][0]:
        if li[i-1][0]==li[i-1][1]:
            cnt+=1
        continue 
    if time>=li[i][1]:
        cnt+=1
        time=li[i][0]
print(cnt)