# TC: O(n * k log k)
# SC: O(n * k)

from collections import defaultdict

def group_anagrams(strs):
    grouped_anagrams = defaultdict(list)

    for s in strs:
        char_count = tuple(sorted(s))
        grouped_anagrams[char_count].append(s)

    return list(grouped_anagrams.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for group in group_anagrams(strs):
        print(group)
