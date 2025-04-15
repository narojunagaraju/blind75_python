# TC O(n)
# SC O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    result = []
    level_order_traversal(root, 0, result)
    return result

def level_order_traversal(root, level, result):
    if root is None:
        return

    if len(result) <= level:
        result.append([])

    result[level].append(root.val)

    level_order_traversal(root.left, level + 1, result)
    level_order_traversal(root.right, level + 1, result)

# Example usage
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = level_order(root)
    for level in result:
        print(level)
