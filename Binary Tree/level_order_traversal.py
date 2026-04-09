from collections import deque


class CreateTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(root):
    if root is None:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
            
if __name__ == "__main__":
    root = CreateTree(1)
    root.left = CreateTree(2)
    root.right = CreateTree(3)
    root.left.left = CreateTree(4)
    root.left.right = CreateTree(5)
    root.right.left = CreateTree(6)
    root.right.right = CreateTree(7)

    print("Level Order Traversal of binary tree is:")
    level_order_traversal(root) 