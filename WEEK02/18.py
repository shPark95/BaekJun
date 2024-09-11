class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def preorder(node):
    if node:
        print(node.value, end='')
        preorder(node.left)
        preorder(node.right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end='')
        inorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end='')

n=int(input())
tree={}

for _ in range(n):
    root, left, right = input().split()
    if root not in tree:
        tree[root] = Node(root)
    if left !='.':
        tree[left] = Node(left)
        tree[root].left = tree[left]
    if right != '.':
        tree[right] = Node(right)
        tree[root].right = tree[right]

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
