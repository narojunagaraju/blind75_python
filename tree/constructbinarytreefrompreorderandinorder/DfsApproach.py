class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    return buildTreeRecursive(preorder, inorder, 0, 0, len(inorder) - 1)


def buildTreeRecursive(preorder, inorder, preIndex, inStart, inEnd):
    if preIndex >= len(preorder) or inStart > inEnd:
        return None

    root_value = preorder[preIndex]
    root = TreeNode(root_value)

    # Find root in inorder
    inIndex = inStart
    for i in range(inStart, inEnd + 1):
        if inorder[i] == root_value:
            inIndex = i
            break

    # Build left and right subtrees
    root.left = buildTreeRecursive(
        preorder,
        inorder,
        preIndex + 1,
        inStart,
        inIndex - 1
    )

    root.right = buildTreeRecursive(
        preorder,
        inorder,
        preIndex + (inIndex - inStart) + 1,
        inIndex + 1,
        inEnd
    )

    return root


# Main equivalent
if __name__ == "__main__":
    preOrder = [3, 9, 20, 15, 7]
    inOrder = [9, 3, 15, 20, 7]

    root = buildTree(preOrder, inOrder)
    print(root.val if root else None)