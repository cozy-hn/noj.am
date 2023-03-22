def f(x):
    return (c-a2)*x**2-a1*x-a0
a2,a1,a0,c,n0=map(int,open(0).read().split())
if f(n0)>=0 and c>=a2:
    if c-a2==0:
        if a1<=0:
            print(1)
        else:
            print(0)
    elif a1/(2*(c-a2)) <= n0:
            print(1)
    elif f(a1/(2*(c-a2))) >= 0 :
        print(1)
    else:
        print(0)
else:
    print(0)