# TC: O(n log n)
# SC: O(1)
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    result_size = 1

    for i in range(1, len(intervals)):
        if intervals[result_size - 1][1] >= intervals[i][0]:
            intervals[result_size - 1][1] = max(intervals[result_size - 1][1], intervals[i][1])
        else:
            intervals[result_size] = intervals[i]
            result_size += 1

    return intervals[:result_size]

# Example usage
if __name__ == "__main__":
    intervals = [[1, 4], [0, 4], [2, 6]]
    merged_intervals = merge_intervals(intervals)
    for interval in merged_intervals:
        print(interval)
