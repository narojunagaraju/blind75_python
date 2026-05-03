class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def kth_smallest(root, k) -> int:
    return in_order_traversal(root, k)


def in_order_traversal(root, count: int) -> int:
    if root is None:
        return -1
    in_order_traversal(root.left, count)
    count -= 1
    if count == 0:
        return root.val
    in_order_traversal(root.right, count)
    return -1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    kThSmallest = kth_smallest(root, 1)
    print(kThSmallest)
