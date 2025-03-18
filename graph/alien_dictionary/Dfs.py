# TC O(N + E)
# SC O(N + E)
from collections import defaultdict


def alien_order(words):
    graph = defaultdict(list)
    visited = defaultdict(int)

    # Build graph
    for word in words:
        for char in word:
            if char not in graph:
                graph[char] = []
            if char not in visited:
                visited[char] = 0

    # Build edges in the graph
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_length = min(len(word1), len(word2))

        for j in range(min_length):
            char1 = word1[j]
            char2 = word2[j]

            if char1 != char2:
                graph[char1].append(char2)
                break

    result = []
    for char in graph:
        if not topologicalSort(char, graph, visited, result):
            return ""

    return ''.join(result[::-1])


def topologicalSort(node, graph, visited, result):
    if visited[node] == 1:  # Cycle detected
        return False
    if visited[node] == 2:  # Node already visited
        return True

    visited[node] = 1
    for neighbor in graph.get(node, []):
        if not topologicalSort(neighbor, graph, visited, result):
            return False

    visited[node] = 2
    result.append(node)

    return True


# Test the function
words = ["wrt", "wrf", "er", "ett", "rftt"]
result = alien_order(words)

if not result:
    print("Invalid order, cycle detected")
else:
    print(f"Alien dictionary order {result}")
