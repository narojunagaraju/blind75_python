# TC O(N)
# SC O(N)

import re

def is_palindrome(s: str) -> bool:
    string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return string == string[::-1]

# Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
