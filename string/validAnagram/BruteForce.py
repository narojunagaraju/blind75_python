# TC O(n log n)
# SC O(1)
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(is_anagram(s, t))