# TC O(V+E)
# SC O(V+E)

from collections import defaultdict


def can_schedule(num_courses, prerequisites):
    graph = defaultdict(list)
    visited = [0] * num_courses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)

    def is_cyclic(course):
        if visited[course] == 2:
            return False

        if visited[course] == 1:
            return True

        visited[course] = 1

        for next_course in graph[course]:
            if is_cyclic(next_course):
                return True

        visited[course] = 2
        return False

    for course in range(num_courses):
        if is_cyclic(course):
            return False

    return True


# Example usage
print(can_schedule(2, [[1, 0]]))
