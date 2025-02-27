# TC O(M*N)
# SC O(N)

def count_ways(m: int, n: int) -> int:
    prev = [0] * n

    for i in range(m):
        temp = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                temp[j] = 1
                continue

            up = prev[j] if i > 0 else 0
            left = temp[j - 1] if j > 0 else 0

            temp[j] = up + left
        prev = temp
    return prev[n - 1]


print(count_ways(3, 2))
