class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s_map = {}
            for c in s:
                s_map[c] = s_map.get(c, 0) + 1
            s_map = frozenset(s_map.items())
            if s_map in anagrams:
                anagrams[s_map].append(s)
            else:
                anagrams[s_map] = [s]
        return list(anagrams.values())