ip=input()
op=[]
ans=[]
priority={'*':2,'/':2,'+':1,'-':1,'(':0}
for i in ip:
    if i.isalpha():
        ans.append(i)
    else:
        while op and i not in '()' and priority[i]<=priority[op[-1]]:
            ans.append(op.pop())
        if i==')':
            while op[-1]!='(':
                ans.append(op.pop())
            op.pop()
        else:
            op.append(i)
while op:
    ans.append(op.pop())
print(''.join(ans))