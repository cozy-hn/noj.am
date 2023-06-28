import sys
b=bytearray(1<<22)
s=''
while True:
    c=sys.stdin.read(1)
    if c.isnumeric():s+=c
    else:
        n=int(s)
        d=n>>3
        r=n&7
        if not b[d]&(1<<r):
            print(n,end=' ')
            b[d]|=1<<r
        s=''
        if c!=' ':break
