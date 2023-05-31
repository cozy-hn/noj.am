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
    print(root,end='')

while True:
    try:
        preorder,inorder=input().split()
        in_idx={}
        for i in range(len(preorder)):
            in_idx[inorder[i]]=i
        postorder(0,len(preorder)-1,0,len(preorder)-1)
        print()
    except:
        break