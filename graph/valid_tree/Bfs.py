# TC: O(V + E)
# SC : O(V)
from collections import deque


def main():
    n = 5
    edges = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4]
    ]

    print(is_valid_tree(n, edges))


def is_valid_tree(n, edges):
    adj_list = {i: [] for i in range(n)}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    visited = [False] * n
    queue = deque([0])

    while queue:
        node = queue.popleft()

        if visited[node]:  # cycle detected
            return False

        visited[node] = True

        for neighbor in adj_list.get(node, []):
            if not visited[neighbor]:
                queue.append(neighbor)

    return all(visited)


if __name__ == "__main__":
    main()
