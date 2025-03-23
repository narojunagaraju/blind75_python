# TC: O(n log n)
# SC: O(n)
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    result = []
    current_interval = intervals[0]

    for i in range(1, len(intervals)):
        if current_interval[1] >= intervals[i][0]:
            current_interval[1] = max(current_interval[1], intervals[i][1])
        else:
            result.append(current_interval)
            current_interval = intervals[i]

    result.append(current_interval)

    return result


if __name__ == "__main__":
    intervals = [[1, 4], [0, 4]]

    merged_intervals = merge_intervals(intervals)
    for interval in merged_intervals:
        print(interval)
