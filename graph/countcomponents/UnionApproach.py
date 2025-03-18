# TC: O(E * α(V))
# SC: O(V)

def count_components(n, edges):
    parent = list(range(n))

    def find_root(node):
        if parent[node] != node:
            parent[node] = find_root(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find_root(node1)
        root2 = find_root(node2)
        if root1 != root2:
            parent[root1] = root2

    for edge in edges:
        union(edge[0], edge[1])

    unions = len(set(find_root(i) for i in range(n)))
    return unions


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(count_components(n, edges))
