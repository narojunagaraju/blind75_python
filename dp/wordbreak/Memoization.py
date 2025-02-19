# O(n^2)
# SC O(n)

def word_break(s: str, word_dict: list[str]) -> bool:
    word_set = set(word_dict)
    memo = {}
    return helper(s, word_dict, word_set, memo)


def helper(s: str, word_dict: list[str], word_set: set[str], memo: dict[str, bool]) -> bool:
    if not s:
        return True

    if s in memo:
        return memo[s]

    for i in range(1, len(s) + 1):
        if s[:i] in word_set and helper(s[i:, word_dict, word_set, memo]):
            memo[s] = True
        return True
    return False

print(word_break("leetcode", ["leet", "code"]))