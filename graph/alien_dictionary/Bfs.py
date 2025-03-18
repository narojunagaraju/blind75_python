# TC O(N + E)
# SC O(N + E)
from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build graph and in-degree
    for word in words:
        for char in word:
            if char not in graph:
                graph[char] = []
            if char not in in_degree:
                in_degree[char] = 0

    # Build graph edges and in-degree
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_length = min(len(word1), len(word2))

        for j in range(min_length):
            char1 = word1[j]
            char2 = word2[j]

            if char1 != char2:
                graph[char1].append(char2)
                in_degree[char2] += 1
                break

    # Perform BFS with topological sort
    queue = deque([char for char, degree in in_degree.items() if degree == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycle
    if len(result) != len(graph):
        return ""

    return ''.join(result)

# Test the function
words = ["wrt", "wrf", "er", "ett", "rftt"]
result = alien_order(words)

if not result:
    print("Invalid order, cycle detected")
else:
    print(f"Alien dictionary order {result}")
