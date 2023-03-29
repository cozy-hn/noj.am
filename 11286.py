from heapq import heappop,heappush
import sys

input=lambda:sys.stdin.readline().rstrip()

heap=[]

for _ in range(int(input())):
    n=int(input())
    if n==0:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap,(abs(n),n))