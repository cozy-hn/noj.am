import sys
input=lambda:sys.stdin.readline().rstrip()
ans=0
while True:
    try:
        a,b=input().split()
        if a=='Es':
            ans+=int(b)*21
        else:
            ans+=int(b)*17
    except:
        break
print(ans)