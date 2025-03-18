# TC: O(V + E)
# SC :O(V)

def count_components(n, edges):
    # Create an adjacency list
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

    # DFS function to explore the graph
    def dfs(start):
        if not visited[start]:
            visited[start] = True
            for neighbor in adj_list.get(start, []):
                dfs(neighbor)

    # Count connected components
    for node in range(n):
        if not visited[node]:
            dfs(node)
            count += 1

    return count


# Example usage
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(count_components(n, edges))
