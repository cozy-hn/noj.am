N,K=map(int,input().split())
num=list(map(int,input()))
stack=[num[0]]
idx=0
tmp=num[0]
for i in num[1:]:
    if stack[-1]<i:
        while stack and stack[-1]<i and idx<K:
            stack.pop()
            idx+=1
    stack.append(i)
    if idx==K:
        break
else:
    stack=stack[:-K+idx]
    print(''.join(map(str,stack)))
    exit()
print(''.join(map(str,stack))+str(''.join(map(str,num[len(stack)+idx:]))))