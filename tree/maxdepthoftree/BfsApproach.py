# TC: O(n)
# SC: O(m)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        depth += 1

    return depth


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    depth = max_depth(root)
    print("Maximum depth of the binary tree:", depth)