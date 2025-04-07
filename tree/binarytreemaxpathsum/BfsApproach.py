# TC: O(n)
# SC: O(m)

from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(root):
    if root is None:
        return 0

    max_sum = float('-inf')
    queue = deque([root])

    while queue:
        current = queue.popleft()
        max_sum = max(max_sum, calculate_path_sum(current))

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return max_sum

def calculate_path_sum(node):
    if node is None:
        return 0

    left_max = max(0, calculate_max_path_sum(node.left))
    right_max = max(0, calculate_max_path_sum(node.right))

    return left_max + right_max + node.val

def calculate_max_path_sum(node):
    if node is None:
        return 0

    left_max = max(0, calculate_max_path_sum(node.left))
    right_max = max(0, calculate_max_path_sum(node.right))

    return max(left_max, right_max) + node.val

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Max Path Sum:", max_path_sum(root))
