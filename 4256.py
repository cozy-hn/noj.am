import sys
input=lambda : sys.stdin.readline().rstrip()


def postorder(p_s,p_e,i_s,i_e):
    if p_s>p_e or i_s>i_e:
        return
    root=preorder[p_s]
    idx=in_idx[root]
    left=idx-i_s
    postorder(p_s+1,p_s+left,i_s,idx-1)
    postorder(p_s+left+1,p_e,idx+1,i_e)
    print(root,end=' ')

for _ in range(int(input())):	
    N=int(input())
    preorder=[*map(int,input().split())]
    inorder=[*map(int,input().split())]
    in_idx=[0]*(N+1)
    for i in range(N):
        in_idx[inorder[i]]=i
    postorder(0,N-1,0,N-1)
    print()