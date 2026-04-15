class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validateBst(root):
    stack = []
    prev_value = float('-inf')

    current = root
    while current is not None or stack:
        # Traverse left subtree
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()

        # Check BST property
        if current.val <= prev_value:
            return False

        prev_value = current.val

        # Move to right subtree
        current = current.right

    return True


# Main equivalent
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(validateBst(root))