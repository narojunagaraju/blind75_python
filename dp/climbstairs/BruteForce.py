# TC O(2^n)
# SC O(n)

def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)


print(climb_stairs(4))
