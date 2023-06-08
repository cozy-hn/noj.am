import sys

input = sys.stdin.readline

MBTI=['ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP','ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENFJ','ENTJ']
MBTI.sort()
dist_dict = {}

def diff(str1,str2):
    cnt = 0
    for i in range(4):
        if str1[i] != str2[i]:
            cnt += 1
    return cnt

for i in range(16):
    for j in range(i,16):
        for k in range(j,16):
            dist_dict[(MBTI[i],MBTI[j],MBTI[k])] = diff(MBTI[i],MBTI[j]) + diff(MBTI[j],MBTI[k]) + diff(MBTI[k],MBTI[i])

for _ in range(int(input())):
    N=int(input())
    ip=list(input().split())
    if N > 32:
        print(0)
        continue
    ip.sort()
    dist=100
    cnt=0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                dist=min(dist, dist_dict[(ip[i],ip[j],ip[k])])
                cnt += 1
    print(dist)