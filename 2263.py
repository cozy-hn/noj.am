import sys
sys.setrecursionlimit(10**6)
N=int(input())
inorder=list(map(int,input().split()))
postorder=list(map(int,input().split()))
in_idx=[0]*(N+1)
for i in range(N):
    in_idx[inorder[i]]=i

def preorder(i_s,i_e,p_s,p_e):
    if i_s>i_e or p_s>p_e or i_s<0 or p_s<0 or i_e>=N or p_e>=N:
        return
    root=postorder[p_e]
    print(root,end=' ')
    if i_s==i_e:
        return
    p=in_idx[root]
    left=p-i_s
    preorder(i_s,p-1,p_s,p_s+left-1)
    preorder(p+1,i_e,p_s+left,p_e-1)
 
preorder(0,N-1,0,N-1)