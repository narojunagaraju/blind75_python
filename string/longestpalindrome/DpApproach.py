# TC: O(n^2)
# SC: O(n^2)

def longest_palindrome(s: str) -> str:
    n = len(s)
    maxlen = float('-inf')
    starting_index = 0
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if solve(s, i, j, dp) and (j - i + 1) > maxlen:
                starting_index = i
                maxlen = j - i + 1

    return s[starting_index:starting_index + maxlen]

def solve(s: str, l: int, r: int, dp: list) -> bool:
    if l >= r:
        return True

    if dp[l][r]:
        return dp[l][r]

    if s[l] == s[r]:
        dp[l][r] = solve(s, l + 1, r - 1, dp)
    else:
        dp[l][r] = False

    return dp[l][r]

# Example usage
if __name__ == "__main__":
    s = "babad"
    print(longest_palindrome(s))  # Expected output: "bab" or "aba"
