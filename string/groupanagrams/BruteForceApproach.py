# TC: O(n * k log k)
# SC: O(n * k)
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)

    for s in strs:
        sorted_str = "".join(sorted(s))
        anagrams[sorted_str].append(s)

    return list(anagrams.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for group in group_anagrams(strs):
        print(group)
