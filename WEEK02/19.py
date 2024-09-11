# 5639 이진 검색 트리

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.val:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)

# 입력 처리
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read
preorder = list(map(int, input().split()))

# 이진 탐색 트리 구성
root = None
for key in preorder:
    root = insert(root, key)

# 후위 순회 출력
postorder(root)





# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.read

# def postorder(Left, Right):
#     if Left > Right:
#         return
    
#     root = preorder[Left]
#     idx = Left + 1

#     while idx <= Right and preorder[idx] < root:
#         idx += 1
    
#     postorder(Left+1, idx-1)
#     postorder(idx, Right)
#     print(root)

# preorder = list(map(int, input().split()))
# postorder(0, len(preorder)-1)


