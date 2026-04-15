class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Global (or outer scope) map
inorder_index_map = {}


def buildTree(preorder, inorder):
    # Build hashmap for quick lookup
    for i, val in enumerate(inorder):
        inorder_index_map[val] = i

    return buildTreeRecursive(preorder, 0, len(preorder) - 1, 0)


def buildTreeRecursive(preorder, preStart, preEnd, inStart):
    if preStart > preEnd:
        return None

    root_value = preorder[preStart]
    root = TreeNode(root_value)

    inIndex = inorder_index_map.get(root_value, 0)
    left_subtree_size = inIndex - inStart

    root.left = buildTreeRecursive(
        preorder,
        preStart + 1,
        preStart + left_subtree_size,
        inStart
    )

    root.right = buildTreeRecursive(
        preorder,
        preStart + left_subtree_size + 1,
        preEnd,
        inIndex + 1
    )

    return root


# Main equivalent
if __name__ == "__main__":
    preOrder = [3, 9, 20, 15, 7]
    inOrder = [9, 3, 15, 20, 7]

    root = buildTree(preOrder, inOrder)
    print(root.val if root else None)