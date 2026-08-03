class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}
        for s in strs:
            strings.setdefault(''.join(sorted(s)), []).append(s)
        return [v for v in strings.values()]
