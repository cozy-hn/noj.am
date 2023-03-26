import sys
input=lambda:sys.stdin.readline().rstrip()
a=b=0
flag=True
for _ in range(int(input())):
    c=input()
    if c=="D":
        a+=1
    else:
        b+=1
    if abs(a-b)==2:
        if flag:
            print(f"{a}:{b}")
            flag=False
if flag:
    print(f"{a}:{b}")