# TC: O(2^n)
# SC: O(n)
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    return len(intervals) - find_max_non_overlapping(0, intervals)

def find_max_non_overlapping(index, intervals):
    if index == len(intervals):
        return 0


    exclude_current = find_max_non_overlapping(index + 1, intervals)

    include_current = 1
    for i in range(index + 1, len(intervals)):
        if intervals[i][0] >= intervals[index][1]:
            include_current += find_max_non_overlapping(i, intervals)
            break

    return max(include_current, exclude_current)


intervals = [
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3],
]

print(erase_overlap_intervals(intervals))
