# TC: O(n log n)
# SC: O(1)

def can_attend_meetings(intervals):
    # Sort intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Check for overlaps
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True

# Test the function with the given intervals
test1 = can_attend_meetings([[0, 5], [5, 10], [15, 20]])  # True
test2 = can_attend_meetings([[7, 10], [2, 4]])  # True
test3 = can_attend_meetings([[1, 3], [2, 4], [5, 7]])  # False

print(test1)
print(test2)
print(test3)
