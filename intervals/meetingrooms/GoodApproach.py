# TC: O(n log n)
# SC: O(n)

import heapq

def can_attend_meetings(intervals):
    if not intervals:
        return True

    # Sort intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to track the end times of ongoing meetings
    min_heap = []
    heapq.heappush(min_heap, intervals[0][1])

    for i in range(1, len(intervals)):
        # If the current meeting starts before the earliest ending meeting, return False
        if intervals[i][0] < min_heap[0]:
            return False
        heapq.heappush(min_heap, intervals[i][1])

    return True

# Test the function with the given intervals
test1 = can_attend_meetings([[0, 5], [5, 10], [15, 20]])  # True
test2 = can_attend_meetings([[7, 10], [2, 4]])  # True
test3 = can_attend_meetings([[1, 3], [2, 4], [5, 7]])  # False

print(test1)
print(test2)
print(test3)
