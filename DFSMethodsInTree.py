
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder: Root, Left, Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Inorder: Left, Root, Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Postorder: Left, Right, Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Create binary tree using KIMIE
root = Node("K")

root.left = Node("I")
root.right = Node("M")

root.left.left = Node("I")
root.left.right = Node("E")


# Display DFS Traversals
print("DFS METHODS IN TREE")

print("Preorder: ", end="")
preorder(root)

print("\nInorder: ", end="")
inorder(root)

print("\nPostorder: ", end="")
postorder(root)

print()
