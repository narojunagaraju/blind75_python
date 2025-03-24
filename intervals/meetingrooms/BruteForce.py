# TC: O(n^2)
# SC: O(n)

def can_attend_meetings(intervals):
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervalOverlap(intervals[i], intervals[j]):
                return False
    return True

def intervalOverlap(interval1, interval2):
    return interval1[0] < interval2[1] and interval1[1] > interval2[0]

# Test the function with the given intervals
test1 = can_attend_meetings([[0, 5], [5, 10], [15, 20]])  # True
test2 = can_attend_meetings([[7, 10], [2, 4]])  # True
test3 = can_attend_meetings([[1, 3], [2, 4], [5, 7]])  # False

print(test1)
print(test2)
print(test3)
