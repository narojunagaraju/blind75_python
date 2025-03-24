# TC: O(n^2)
# SC: O(n)
def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    min_rooms = float('inf')

    for i in range(len(intervals)):
        current_interval = intervals[i]
        rooms_needed = 1

        for j in range(len(intervals)):
            if i != j:
                other_interval = intervals[j]
                # Check if the intervals overlap
                if current_interval[0] < other_interval[1] and current_interval[1] > other_interval[0]:
                    rooms_needed += 1

        min_rooms = min(min_rooms, rooms_needed)

    return min_rooms


# Test the function with the given intervals
test1 = min_meeting_rooms([[0, 30], [5, 10], [15, 20]])  # 2
test2 = min_meeting_rooms([[7, 10], [2, 4]])  # 1
test3 = min_meeting_rooms([[1, 5], [2, 6], [3, 7]])  # 3
test4 = min_meeting_rooms([[1, 3], [2, 4], [3, 6]])  # 2

print(f"Test 1: {test1}")
print(f"Test 2: {test2}")
print(f"Test 3: {test3}")
print(f"Test 4: {test4}")

