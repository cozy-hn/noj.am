import sys
input=sys.stdin.readline
N,M=map(int,input().split())
truth=set(list(map(int,input().split()))[1:])
partys=[list(map(int,input().split()))[1:] for _ in range(M)]
lie=[]
    
for party in partys:
    for i in party:
        if i in truth:
            break
    else:
        lie.append(party)
        continue
    for i in party:
        truth.add(i)

while True:
    lienum=len(lie)
    for party in lie:
        for i in party:
            if i in truth:
                break
        else:
            continue
        lie.remove(party)
        for i in party:
            truth.add(i)
    if lienum==len(lie):
        break
print(len(lie))
