import sys
input=sys.stdin.readline
N=int(input())
first=list(map(int,input().split()))
MAX=first
MIN=first[:]
for i in range(N-1):
    a,b,c=map(int,input().split())
    MAX=[max(MAX[0],MAX[1])+a,max(MAX[0],MAX[1],MAX[2])+b,max(MAX[1],MAX[2])+c]
    MIN=[min(MIN[0],MIN[1])+a,min(MIN[0],MIN[1],MIN[2])+b,min(MIN[1],MIN[2])+c]
print(max(MAX),min(MIN))