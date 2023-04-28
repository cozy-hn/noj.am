class tree():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

N=int(input())
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
node=[tree(capital[i]) for i in range(N)]
for _ in range(N):
    a,b,c=input().split()
    node[capital.index(a)].left = node[capital.index(b)] if b != '.' else None
    node[capital.index(a)].right = node[capital.index(c)] if c != '.' else None

def preorder(node):
    print(node.val, end='')
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.val, end='')
    if node.right:
        inorder(node.right)

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.val, end='')
    
preorder(node[0])
print()
inorder(node[0])
print()
postorder(node[0])
    
    
