# TC O(2^n)
# SC O(n)

def word_break(s: str, word_dict: list[str]) -> bool:
    word_set = set(word_dict)  # Convert word list to a set for quick lookup
    return word_break_helper(s, word_set)


def word_break_helper(s: str, word_set: set[str]) -> bool:
    if not s:
        return True

    for i in range(1, len(s) + 1):
        if s[:i] in word_set and word_break_helper(s[i:], word_set):
            return True

    return False


print(word_break("leetcode", ["leet", "code"]))
