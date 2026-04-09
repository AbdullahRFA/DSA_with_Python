'''
Level Order Traversal of a binary tree is a breadth-first traversal method where we visit all the nodes at the present depth level before moving on to the nodes at the next depth level. This can be implemented using a queue data structure to keep track of the nodes to be visited.
In the provided code, we define a class `CreateTree` to represent each node in the binary tree. The `level_order_traversal` function takes the root of the tree as input and uses a queue to perform the level order traversal. It prints the data of each node as it is visited.
The example at the end of the code creates a binary tree with 7 nodes and calls the `level_order_traversal` function to print the nodes in level order. The expected output will be:
```Level Order Traversal of binary tree is:
1 2 3 4 5 6 7 ```

time complexity: O(n) where n is the number of nodes in the binary tree, as we visit each node exactly once.
space complexity: O(n) in the worst case, when the binary tree is completely unbalanced (like a linked list), the queue can hold all the nodes at once. In the best case, when the tree is perfectly balanced, the space complexity is O(w) where w is the maximum width of the tree (the maximum number of nodes at any level).
'''


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