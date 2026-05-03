# Example usage
from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def kth_smallest(root, k) -> int:
    queue = deque()
    queue.append(root)
    values = []
    while queue:
        node = queue.popleft()
        values.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    if k <= len(values):
        values.sort()
        return values[k - 1]
    return -1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    kThSmallest = kth_smallest(root, 1)
    print(kThSmallest)
