import copy
from heapq import heappush, heappop

row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

class node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level
        # self.move = move

    def __lt__(self, nxt):
        return self.cost < nxt.cost

def calculateCost(mat, final):
    count = 0
    for i in range(3):
        for j in range(3):
            if (mat[i][j] and mat[i][j] != final[i][j]):
                count += 1
    return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final):
    new_mat = copy.deepcopy(mat)

    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]
    x2 = new_empty_tile_pos[0]
    y2 = new_empty_tile_pos[1]
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    cost = calculateCost(new_mat, final)
    new_node = node(parent, new_mat, new_empty_tile_pos,cost, level)
    return new_node

def printMatrix(mat):
    
    for i in range(3):
        for j in range(3):
            print("%d " % (mat[i][j]), end = " ")
        print()

def isSafe(x, y):
    return x >= 0 and x < 3 and y >= 0 and y < 3

def printPath(root):
    if root == None:
        return
    printPath(root.parent)
    # if root.move != 0:
    printMatrix(root.mat)
        # print(root.move, end=' ')
    print()

def solve(initial, empty_tile_pos, final):

    pq = []
    cost = calculateCost(initial, final)
    root = node(None, initial, empty_tile_pos, cost, 0)
    heappush(pq, root)

    while pq:
        minimum = heappop(pq)
        if minimum.cost == 0:
            print(minimum.level)
            printPath(minimum)
            return
        for i in range(4):
            new_tile_pos = (minimum.empty_tile_pos[0] + row[i], minimum.empty_tile_pos[1] + col[i])
            if isSafe(new_tile_pos[0], new_tile_pos[1]):
                child = newNode(minimum.mat, minimum.empty_tile_pos, new_tile_pos, minimum.level + 1, minimum, final)
                heappush(pq,child)

# initial = []
# for i in range(3):
#     tmp=input().split()
#     for j in range(3):
#         if tmp[j]=='X':
#             empty_tile_pos=(i,j)
#             tmp[j]='0'
#     initial.append(list(map(int,tmp)))
        
initial = [ [ 1, 2, 3 ],
			[ 4, 6, 8 ],
			[ 7, 5, 0 ] ]

final = [ [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 0 ] ]

empty_tile_pos = [ 2, 2 ]
solve(initial, empty_tile_pos, final)
