# TC: O(n log n)
# SC: O(n)

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    # Separate the start and end times
    start_times = [interval[0] for interval in intervals]
    end_times = [interval[1] for interval in intervals]

    # Sort the start and end times
    start_times.sort()
    end_times.sort()

    rooms = 0
    end_pointer = 0

    # Iterate over the start times
    for start in start_times:
        # If a meeting starts before the earliest ending meeting, we need a new room
        if start < end_times[end_pointer]:
            rooms += 1
        else:
            end_pointer += 1

    return rooms

# Test the function with the given intervals
test1 = min_meeting_rooms([[0, 30], [5, 10], [15, 20]])  # 2
test2 = min_meeting_rooms([[7, 10], [2, 4]])  # 1
test3 = min_meeting_rooms([[1, 5], [2, 6], [3, 7]])  # 3
test4 = min_meeting_rooms([[1, 3], [2, 4], [3, 6]])  # 2

print(f"Test 1: {test1}")
print(f"Test 2: {test2}")
print(f"Test 3: {test3}")
print(f"Test 4: {test4}")
