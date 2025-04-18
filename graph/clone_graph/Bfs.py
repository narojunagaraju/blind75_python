# TC O(V+E)
# SC O(V+E)

from collections import deque
from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: 'Node') -> Optional[Node]:
    if node is None:
        return None

    node_map = {}
    queue = deque([node])
    node_map[node] = Node(node.val)

    while queue:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in node_map:
                node_map[neighbor] = Node(neighbor.val)
                queue.append(neighbor)

            node_map[current].neighbors.append(node_map[neighbor])

    return node_map[node]


# Client code to test clone_graph function
def print_graph(node: Node):
    """Helper function to print the graph for verification"""
    visited = set()
    queue = deque([node])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        print(f"Node {current.val}: {[neighbor.val for neighbor in current.neighbors]}")

        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)


# Creating a sample graph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Cloning the graph
cloned_graph = clone_graph(node1)

# Printing original and cloned graphs
print("Original Graph:")
print_graph(node1)

print("\nCloned Graph:")
print_graph(cloned_graph)

