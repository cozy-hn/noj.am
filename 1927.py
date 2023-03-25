import sys
from queue import PriorityQueue

input=lambda : sys.stdin.readline().rstrip()

q=PriorityQueue()
for _ in range(int(input())):
    n=int(input())
    if n==0:
        if q.empty():
            print(0)
        else:
            print(q.get())
    else:
        q.put(n)