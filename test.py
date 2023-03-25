import sys
from queue import PriorityQueue

input=lambda:sys.stdin.readline().rstrip()

q=PriorityQueue()
q.put(1)
print(q.get())
q.get()