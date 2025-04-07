# TC: O(n)
# SC: O(h)

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(root):
    max_sum = float('-inf')  # Declare inside to allow `nonlocal` usage

    def max_path(node):
        nonlocal max_sum
        if node is None:
            return 0

        left_max = max(0, max_path(node.left))
        right_max = max(0, max_path(node.right))

        max_sum = max(max_sum, left_max + right_max + node.val)

        return max(left_max, right_max) + node.val

    max_path(root)
    return max_sum

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Max Path Sum:", max_path_sum(root))
