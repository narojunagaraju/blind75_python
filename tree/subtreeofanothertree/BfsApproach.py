from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(s, t):
    s_queue = deque([s])

    while s_queue:
        current = s_queue.popleft()

        if current:
            if isSameTree(current, t):
                return True

            s_queue.append(current.left)
            s_queue.append(current.right)

    return False


def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    queue = deque([(p, q)])

    while queue:
        node_p, node_q = queue.popleft()

        if (node_p.val if node_p else None) != (node_q.val if node_q else None):
            return False

        if node_p:
            queue.append((node_p.left, node_q.left if node_q else None))
            queue.append((node_p.right, node_q.right if node_q else None))

    return True


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