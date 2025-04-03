# TC O(N)
# SC O(N)
import re

def is_palindrome(s: str) -> bool:
    string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    left, right = 0, len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

# Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
