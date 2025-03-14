# TC O(V+E)
# SC O(V+E)

from collections import defaultdict, deque

def can_schedule(num_courses, prerequisites):
    in_degree = [0] * num_courses
    graph = defaultdict(list)

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        in_degree[course] += 1

    queue = deque()

    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        current_course = queue.popleft()

        for neighbor in graph[current_course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return all(degree == 0 for degree in in_degree)


print(can_schedule(2, [[1, 0]]))
