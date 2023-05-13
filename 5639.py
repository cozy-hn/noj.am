import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
Tree={}
root=int(input())
Tree[root]=[None,None]

def pushtree(node,r=root):
    if node<r:
        if Tree[r][0]==None:
            Tree[r][0]=node
            Tree[node]=[None,None]
        else:
            pushtree(node,Tree[r][0])
    else:
        if Tree[r][1]==None:
            Tree[r][1]=node
            Tree[node]=[None,None]
        else:
            pushtree(node,Tree[r][1])

while True:
    try:
        pushtree(int(input()))
    except:
        break
    
def postorder(node):
    if Tree[node][0]:
        postorder(Tree[node][0])
    if Tree[node][1]:
        postorder(Tree[node][1])
    print(node)

postorder(root)
