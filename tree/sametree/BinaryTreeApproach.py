# TC: O(n)
# SC: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order_traversal(root: TreeNode, result: list):
    if root is None:
        result.append(None)
        return
    result.append(root.val)
    pre_order_traversal(root.left, result)
    pre_order_traversal(root.right, result)

def same_tree(root1: TreeNode, root2: TreeNode) -> bool:
    list_a = []
    list_b = []
    pre_order_traversal(root1, list_a)
    pre_order_traversal(root2, list_b)
    return list_a == list_b

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    print(same_tree(root1, root2))
