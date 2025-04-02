# TC O(n)
# SC O(1)

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_count = [0] * 128  # ASCII character set size

    for char in s:
        char_count[ord(char)] += 1

    for char in t:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False

    return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(is_anagram(s, t))