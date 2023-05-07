N,A=map(int, input().split())
B=N-A

def e_gcd(a, b):
    x, y, u, v = 1, 0, 0, 1

    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, u = u, x - q * u
        y, v = v, y - q * v

    return a, x, y

gcd, C, _= e_gcd(A,N)
if C<0:
	C+=N
if gcd!=1:
    C=-1

print(B,C)