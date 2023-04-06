ip=input()
hey=input()
heylen=len(hey)
li=[]
cnt=0
for i in ip:
    li.append(i)
    if i==hey[-1] and len(li)>=heylen:
        if ''.join(li[-heylen:])==hey:
            for i in range(heylen):
                li.pop()
if not li:
    print('FRULA')
else:
    print(''.join(li))