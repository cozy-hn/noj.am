import sys
from collections import deque

input= lambda : sys.stdin.readline().rstrip()
for _ in range(int(input())):
    order=list(input())
    N=int(input())
    str_=input()
    str_=str_.replace('[',',')
    str_=str_.replace(']',',')
    li=list(str_.split(','))
    flag=0
    if N:
        dq=deque(map(int,li[1:-1]))
    else:
        if 'D' in order:
            print('error')
        else:
            print('[]')
        continue
    for i in order:
        if i=='R':
            flag+=1
        if i=='D':
            if dq:
                if flag%2:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                print('error')
                flag=-1
                break
    if flag==-1:
        continue
    if flag%2:
        dq.reverse()
    print('[',end='')
    print(*dq,sep=',',end='')
    print(']')