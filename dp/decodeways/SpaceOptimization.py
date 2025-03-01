# TC O(n)
# SC O(1)

def decode_ways(s: str) -> int:
    n = len(s)
    next = 1
    next2 = 0

    for i in range(n-1, -1, -1):
        curr = next
        if s[i] != '0':
            if i < n - 1 and int(s[i:i + 2]) <= 26:
                curr += next2
        else:
            curr = 0

        next2 = next
        next = curr

    return next

print(decode_ways("12"))
