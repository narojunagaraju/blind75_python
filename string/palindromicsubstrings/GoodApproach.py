# TC: O(n^2)
# SC: O(1)

def main():
    s = "abc"
    print(count_substrings(s))

def count_substrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        count += expand_around_center(s, i, i)       # Odd-length palindromes
        count += expand_around_center(s, i, i + 1)   # Even-length palindromes
    return count

def expand_around_center(s: str, left: int, right: int) -> int:
    l, r = left, right
    count = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1
    return count

if __name__ == "__main__":
    main()
