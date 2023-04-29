import sys
input=lambda: sys.stdin.readline().rstrip()
SET={'ChongChong'}
for _ in range(int(input())):
    a,b=input().split()
    if a in SET or b in SET:
        SET.add(a)
        SET.add(b)
print(len(SET))