# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: TreeNode) -> str:
    result = []

    def serialize_dfs(node):
        if not node:
            result.append("null")
            return
        result.append(str(node.val))
        serialize_dfs(node.left)
        serialize_dfs(node.right)

    serialize_dfs(root)
    return ','.join(result)

def deserialize(data: str) -> TreeNode:
    nodes = deque(data.split(','))

    def deserialize_dfs():
        if not nodes:
            return None
        val = nodes.popleft()
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = deserialize_dfs()
        node.right = deserialize_dfs()
        return node

    return deserialize_dfs()

# Main equivalent
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    serialized = serialize(root)
    print(serialized)
    deserialized = deserialize(serialized)
    print(deserialized.right.right.val if deserialized and deserialized.right and deserialized.right.right else None)
