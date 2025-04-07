# TC: O(n)
# SC: O(m)

from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def invert_tree(root):
    if root is None:
        return None

    queue = deque([root])

    while queue:
        current = queue.popleft()

        # Swap left and right children
        current.left, current.right = current.right, current.left

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return root

def print_tree_level_order(root):
    if not root:
        print("Tree is empty")
        return

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print("Level order:", result)

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    invertedRoot = invert_tree(root)
    print_tree_level_order(invertedRoot)
