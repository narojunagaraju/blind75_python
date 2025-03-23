# TC: O(n)
# SC: O(n)
def insert(intervals, new_interval):
    result = []
    inserted = False

    for interval in intervals:
        if interval[1] < new_interval[0]:
            result.append(interval)
        elif interval[0] > new_interval[1]:
            if not inserted:
                result.append(new_interval)
                inserted = True
            result.append(interval)
        else:
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])

    if not inserted:
        result.append(new_interval)

    return result


# Example input
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]

# Call the insert function and print the result
result = insert(intervals, new_interval)
print("Updated intervals:", result)
