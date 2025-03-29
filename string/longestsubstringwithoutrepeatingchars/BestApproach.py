# TC: O(n)
# SC: O(min(n, m))

def length_of_longest_substring(s: str) -> int:
    res = {}
    maxlen = 0
    i = 0

    for j in range(len(s)):
        if s[j] in res and res[s[j]] >= i:
            i = res[s[j]] + 1
        res[s[j]] = j
        maxlen = max(maxlen, j - i + 1)

    return maxlen

print(length_of_longest_substring("abcabcbb"))
