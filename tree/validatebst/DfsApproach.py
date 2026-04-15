class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validateBst(root):
    return isValidBstHelper(root, float('-inf'), float('inf'))


def isValidBstHelper(root, minValue, maxValue):
    if root is None:
        return True

    if root.val <= minValue or root.val >= maxValue:
        return False

    return (
        isValidBstHelper(root.left, minValue, root.val) and
        isValidBstHelper(root.right, root.val, maxValue)
    )


# Main equivalent
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(validateBst(root))