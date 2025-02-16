# TC O(n*m)
# SC O(m)

def lcs(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)

    # Base Case: prev and cur are initialized to 0 by default
    prev = [0] * (m + 1)
    cur = [0] * (m + 1)

    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                cur[ind2] = 1 + prev[ind2 - 1]
            else:
                cur[ind2] = max(prev[ind2], cur[ind2 - 1])

        # Move cur to prev for the next iteration
        prev = cur[:]

    return prev[m]


s1 = "abcde"
s2 = "ace"
print(lcs(s1, s2))
