from collections import deque

# Diagram 1: Binary Tree
#
#            B
#          /   \
#         A     R
#        / \   / \
#       T   I D   O


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BFS (level order) using a queue
def bfs(root):
    if root is None:
        return "Tree is empty"

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return " - ".join(result)


# DFS (preorder: node, left, right) using recursion
def dfs(node, result):
    if node is None:
        return
    result.append(node.value)
    dfs(node.left, result)
    dfs(node.right, result)


def get_results():
    b = Node("B")
    a = Node("A")
    r = Node("R")
    t = Node("T")
    i = Node("I")
    d = Node("D")
    o = Node("O")

    b.left, b.right = a, r
    a.left, a.right = t, i
    r.left, r.right = d, o

    dfs_result = []
    dfs(b, dfs_result)
    return bfs(b), " - ".join(dfs_result)


def run():
    bfs_text, dfs_text = get_results()
    print("=== Binary Tree ===")
    print("BFS:", bfs_text)
    print("DFS:", dfs_text)


if __name__ == "__main__":
    run()