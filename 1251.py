s=list(input())
Len=len(s)
ret=[]
for i in range(1,Len-1):
    for j in range(i+1,Len):
        a=s[:i]
        b=s[i:j]
        c=s[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        ret.append(''.join(a+b+c))
ret.sort()
print(ret[0])