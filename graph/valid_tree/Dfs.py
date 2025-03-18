# TC: O(V + E)
# SC : O(V)

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
    if has_cycle(adj_list, 0, -1, visited):
        return False

    return all(visited)


def has_cycle(adj_list, node, parent, visited):
    visited[node] = True

    for neighbor in adj_list.get(node, []):
        if not visited[neighbor]:
            if has_cycle(adj_list, neighbor, node, visited):
                return True
        elif neighbor != parent:
            return True  # back edge detected

    return False


if __name__ == "__main__":
    main()
