# TC: O(n^2)
# SC: O(1)


def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""

    start, end = 0, 0

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)

        if length > (end - start):
            start = i - (length - 1) // 2
            end = i + length // 2

    return s[start:end + 1]

def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1  # Length of the palindrome

# Example usage
print(longest_palindromic_substring("babad"))  # "bab" or "aba"
print(longest_palindromic_substring("cbbd"))   # "bb"
