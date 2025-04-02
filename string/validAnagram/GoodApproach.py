# TC O(n)
# SC O(1)

from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(is_anagram(s, t))