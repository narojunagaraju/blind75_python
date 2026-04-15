class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(s, t):
    if s is None:
        return False

    return (
        isSameTree(s, t) or
        isSubtree(s.left, t) or
        isSubtree(s.right, t)
    )


def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None or p.val != q.val:
        return False

    return (
        isSameTree(p.left, q.left) and
        isSameTree(p.right, q.right)
    )


# Main equivalent
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    print(isSubtree(root, subRoot))