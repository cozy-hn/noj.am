import re
str_=input()
li=re.split('([+|-])', str_)
ans=0
flag=False
for i in li:
    if i=='-':
        flag=True
    elif i=='+':
        continue
    else:
        if flag:
            ans-=int(i)
        else:
            ans+=int(i)
print(ans)