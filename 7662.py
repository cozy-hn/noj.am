import sys
from heapq import heappop,heappush

input=lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())):
    heapM=[]
    heapm=[]
    n=int(input())
    visit=[0]*(n+1)
    for i in range(n):
        cmd,num=input().split()
        if cmd=='I':
            num=int(num)
            heappush(heapM,(-num,i))
            heappush(heapm,(num,i))
        elif cmd=='D':
            if num=='1':
                while heapM and visit[heapM[0][1]]:
                    heappop(heapM)
                if heapM:
                    visit[heappop(heapM)[1]]=1
                    
            else:
                while heapm and visit[heapm[0][1]]:
                    heappop(heapm)
                if heapm:
                    visit[heappop(heapm)[1]]=1
    while heapM and visit[heapM[0][1]]:
        heappop(heapM)
    while heapm and visit[heapm[0][1]]:
        heappop(heapm)
    if not heapM or not heapm:
        print('EMPTY')
    else:
        print(-heappop(heapM)[0],heappop(heapm)[0])
