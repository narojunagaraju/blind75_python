# O(n^2)
# SC O(n)

def word_break(s: str, word_dict: list[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for length in range(1, n + 1):
        for i in range(length):
            if dp[i] and s[i:length] in word_dict:
                dp[length] = True
                break
    return dp[n]
