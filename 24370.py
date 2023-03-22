def f1(x):
    return (c1-a2)*x**2-a1*x-a0
def f2(x):
    return (c2-a2)*x**2-a1*x-a0
a2,a1,a0,c1,c2,n0=map(int,open(0).read().split())
flag1=0
flag2=0
if f1(n0)<=0 and c1<=a2:
    if c1-a2==0:
        if a1>=0:
            flag1=1
    elif a1/(2*(c1-a2)) <= n0:
        flag1=1
    elif f1(a1/(2*(c1-a2))) <= 0 :
        flag1=1
if f2(n0)>=0 and c2>=a2:
    if c2-a2==0:
        if a1<=0:
            flag2=1
    elif a1/(2*(c2-a2)) <= n0:
        flag2=1
    elif f2(a1/(2*(c2-a2))) >= 0 :
        flag2=1
if flag1 and flag2:
    print(1)
else:
    print(0)