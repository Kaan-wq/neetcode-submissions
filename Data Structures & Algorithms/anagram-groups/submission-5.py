class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        shash = {}

        for s in strs:
            hist = [0] * 26

            for c in s:
                hist[ord(c) - ord("a")] += 1
            
            shash.setdefault(tuple(hist), []).append(s)

        return list(shash.values())