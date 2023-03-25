import sys
from heapq import heappush, heappop
input=lambda:sys.stdin.readline().rstrip()
heap=[]
for _ in range(int(input())):
    n=int(input())
    if n!=0:
        heappush(heap,(-n,n))
    elif heap:
        print(heappop(heap)[1])
    else:
        print(0)