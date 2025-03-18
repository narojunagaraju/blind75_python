# TC: O(V + E)
# SC :O(V)

from collections import deque


def count_components(n, edges):
    adj_list = {}

    for edge in edges:
        if edge[0] not in adj_list:
            adj_list[edge[0]] = []
        if edge[1] not in adj_list:
            adj_list[edge[1]] = []
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    visited = [False] * n
    count = 0

    for node in range(n):
        if not visited[node]:
            bfs(node, visited, adj_list)
            count += 1

    return count


def bfs(start, visited, adj_list):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        for neighbor in adj_list.get(current, []):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(count_components(n, edges))
