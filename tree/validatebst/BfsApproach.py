from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeBounds:
    def __init__(self, node, lower_bound, upper_bound):
        self.node = node
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound


def validateBst(root):
    if root is None:
        return True

    queue = deque([NodeBounds(root, float('-inf'), float('inf'))])

    while queue:
        current = queue.popleft()
        node = current.node
        lower = current.lower_bound
        upper = current.upper_bound

        if node.val <= lower or node.val >= upper:
            return False

        if node.left:
            queue.append(NodeBounds(node.left, lower, node.val))

        if node.right:
            queue.append(NodeBounds(node.right, node.val, upper))

    return True


# Main equivalent
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(validateBst(root))