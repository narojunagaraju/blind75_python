class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def kth_smallest(root, k) -> int:
    if root is None:
        return -1
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()

        k -= 1  # Use k directly
        if k == 0:
            return current.val
        current = current.right

    return -1

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    kthSmallest = kth_smallest(root, 2)
    print(kthSmallest)
