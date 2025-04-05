# TC: O(n^3)
# SC: O(1)

def main():
    s = "abc"
    print(count_substrings(s))

def count_substrings(s: str) -> int:
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i:j + 1]):
                res += 1
    return res

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == "__main__":
    main()
