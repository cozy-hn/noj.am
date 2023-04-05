import sys
from collections import deque
from string import ascii_uppercase

input=lambda: sys.stdin.readline().rstrip()
alpha_list = list(ascii_uppercase)
alpha_dic={}
N=int(input())
dq=deque(input())
for i in range(N):
    alpha_dic[alpha_list[i]]=int(input())
li=[]
while dq:
    t=dq.popleft()
    if t.isalpha():
        li.append(alpha_dic[t])
    else:
        a,b=li.pop(),li.pop()
        if t=='+':
            li.append(a+b)
        elif t=='-':
            li.append(b-a)
        elif t=='*':
            li.append(a*b)
        else:
            li.append(b/a)
print(f'{li[-1]:.2f}')