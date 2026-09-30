class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for s in strs:
            l = [0 for _ in range(26)]
            for c in s:
                l[ord(c) - ord("a")] += 1
            a.setdefault(tuple(l), []).append(s)
        return list(a.values())