# Time Complexity: O(n)
# Space Complexity: O(n)
from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def serialize(root: TreeNode) -> str:
    result = []
    queue = deque()

    if root:
        queue.append(root)

    while queue:
        current = queue.popleft()

        if current is None:
            result.append("null")
            continue

        result.append(str(current.val))
        queue.append(current.left)
        queue.append(current.right)

    return ','.join(result)

def deserialize(data: str) -> TreeNode:
    nodes = deque(data.split(","))
    if not nodes or nodes[0] == "" or nodes[0] == "null":
        return None

    root = TreeNode(int(nodes.popleft()))
    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()

        if nodes:
            left_val = nodes.popleft()
            if left_val != "null":
                current.left = TreeNode(int(left_val))
                queue.append(current.left)

        if nodes:
            right_val = nodes.popleft()
            if right_val != "null":
                current.right = TreeNode(int(right_val))
                queue.append(current.right)

    return root

# Equivalent of Kotlin `main`
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    serialized = serialize(root)
    print(serialized)

    deserialized = deserialize(serialized)
    if deserialized and deserialized.right and deserialized.right.right:
        print(deserialized.right.right.val)
    else:
        print(None)
