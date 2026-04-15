class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildtree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    stack = [root]

    inorder_index = 0

    for i in range(1, len(preorder)):
        current_node = None
        new_node = TreeNode(preorder[i])

        while stack and stack[-1].val == inorder[inorder_index]:
            current_node = stack.pop()
            inorder_index += 1

        if current_node:
            current_node.right = new_node
        else:
            stack[-1].left = new_node

        stack.append(new_node)

    return root


# Main equivalent
if __name__ == "__main__":
    preOrder = [3, 9, 20, 15, 7]
    inOrder = [9, 3, 15, 20, 7]

    root = buildtree(preOrder, inOrder)
    print(root.val if root else None)