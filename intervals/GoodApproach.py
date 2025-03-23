# TC: O(n)
# SC: O(n)
def insert(intervals, new_interval):
    result = []
    i = 0

    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    input_intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]

    result = insert(input_intervals, new_interval)
    for interval in result:
        print(interval)
