from heapq import heappush, heappop
def solution(k, n, reqs):
    ans=0
    case=[]
    mkcase(n, k, case)
    ans=min(caltime(n,k,reqs,mento) for mento in case)
    return ans

def mkcase(n, k, case, csum=0, ele=[]):
    if len(ele) > k or csum > n:
        return
    if len(ele) == k and csum == n:
        case.append(ele[:])
        return

    for i in range(1, n+1):
        ele.append(i)
        mkcase(n, k, case, csum+i, ele)
        ele.pop()

def caltime(n,k,reqs,mento):
    time=0
    mentoroom=[[0]*i for i in mento]
    for req in reqs:
        start, dur, room = req
        room-=1
        end=start+dur
        wait=0
        if mentoroom[room][0] > start:
                wait=mentoroom[room][0]-start
                time+=(wait)
        heappop(mentoroom[room])
        heappush(mentoroom[room],end+wait)
    return time

n,k=map(int,input().split())
reqs=[]
while True:
    try:
        reqs.append(list(map(int,input().split())))
    except:
        break
print(solution(k, n, reqs))
