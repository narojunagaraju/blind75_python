# TC: O(n^3)
# SC: O(1)

def longest_palindromic_substring(s: str) -> str:
    longest_palindrome = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            if is_palindrome(sub_string) and len(sub_string) > len(longest_palindrome):
                longest_palindrome = sub_string

    return longest_palindrome

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Example usage
print(longest_palindromic_substring("babad"))  # "bab" or "aba"
print(longest_palindromic_substring("cbbd"))   # "bb"
