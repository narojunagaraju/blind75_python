# TC: O(n log n)
# SC: O(n)
import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    # Sort intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to track the end times of ongoing meetings
    min_heap = []
    heapq.heappush(min_heap, intervals[0][1])

    for i in range(1, len(intervals)):
        # If the current meeting starts after the earliest ending meeting, remove the old meeting from heap
        if intervals[i][0] >= min_heap[0]:
            heapq.heappop(min_heap)

        # Add the current meeting's end time to the heap
        heapq.heappush(min_heap, intervals[i][1])

    return len(min_heap)


# Test the function with the given intervals
test1 = min_meeting_rooms([[0, 30], [5, 10], [15, 20]])  # 2
test2 = min_meeting_rooms([[7, 10], [2, 4]])  # 1
test3 = min_meeting_rooms([[1, 5], [2, 6], [3, 7]])  # 3
test4 = min_meeting_rooms([[1, 3], [2, 4], [3, 6]])  # 2

print(f"Test 1: {test1}")
print(f"Test 2: {test2}")
print(f"Test 3: {test3}")
print(f"Test 4: {test4}")
