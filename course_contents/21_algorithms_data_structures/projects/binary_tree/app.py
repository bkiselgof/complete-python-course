from binary_tree import BinaryTree
from node import Node

tree = BinaryTree(Node(6))

nodes = [5, 3, 9, 7, 8, 7.5, 12, 11]

for n in nodes:
    tree.add(Node(n))

tree.delete(9)
tree.inorder()


#######
from node import Node
left = Node(5)
head = Node(9)
right = Node(13)

head.left = left
head.right = right

print(head)
print(head.left)
print(head.right)