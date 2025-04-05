# TC: O(n)
# SC: O(n)

def main():
    s = "abc"
    print(count_substrings(s))

def count_substrings(s: str) -> int:
    modified_string = build_modified_string(s)
    p = [0] * len(modified_string)
    count = 0
    c = 0
    r = 0

    for i in range(1, len(modified_string) - 1):
        mirror = 2 * c - i

        if i < r:
            p[i] = min(r - i, p[mirror])

        # Attempt to expand palindrome centered at i
        a = i + (1 + p[i])
        b = i - (1 + p[i])

        while a < len(modified_string) and b >= 0 and modified_string[a] == modified_string[b]:
            p[i] += 1
            a += 1
            b -= 1

        # If palindrome centered at i expands past right boundary, adjust center and right boundary
        if i + p[i] > r:
            c = i
            r = i + p[i]

        # Count the palindromes centered at i
        count += (p[i] + 1) // 2

    return count

def build_modified_string(s: str) -> str:
    sb = "#"
    for char in s:
        sb += char + "#"
    return sb

if __name__ == "__main__":
    main()
