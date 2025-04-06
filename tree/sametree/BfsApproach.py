# TC: O(n)
# SC: O(n)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def same_tree(root1: TreeNode, root2: TreeNode) -> bool:
    queue = deque()
    queue.append(root1)
    queue.append(root2)

    while queue:
        nodeA = queue.popleft()
        nodeB = queue.popleft()

        if not nodeA and not nodeB:
            continue

        if not nodeA or not nodeB or nodeA.val != nodeB.val:
            return False

        queue.append(nodeA.left)
        queue.append(nodeB.left)
        queue.append(nodeA.right)
        queue.append(nodeB.right)

    return True

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    print(same_tree(root1, root2))
