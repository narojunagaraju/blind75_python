# TC O(n)
# SC O(n)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            current = queue.popleft()
            level_nodes.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        result.append(level_nodes)

    return result

# Main
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = level_order(root)
    for level in result:
        print(level)
