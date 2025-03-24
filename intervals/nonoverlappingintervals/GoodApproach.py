# TC: O(n log n)
# SC: O(1)

def erase_overlap_intervals(intervals):
    if not intervals:
        return 0

    # Sort intervals by their end time
    intervals.sort(key=lambda x: x[1])

    count = 1
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]

    return len(intervals) - count

# Test the function with the given intervals
intervals = [
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3],
]

print(erase_overlap_intervals(intervals))
