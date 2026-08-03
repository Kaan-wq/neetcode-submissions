class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}
        for s in strs:
            ss = ''.join(sorted(s))
            strings.setdefault(ss, []).append(s)
        return [v for v in strings.values()]
