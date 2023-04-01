N,K=map(int,input().split())
U=1
D=1
for i in range(K):
    U=(U*(N-i)%1000000007)
    D=(D*(i+1)%1000000007)

def power(num, p, mod):
    if p == 1:
        return num % mod
    
    if p % 2:
        return ((power(num,p//2,mod) ** 2) * num) % mod
    else:
        return (power(num,p//2,mod) ** 2) % mod
    
print(((U)*(power(D,1000000005,1000000007)))%1000000007)
