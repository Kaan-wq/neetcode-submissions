class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = {}
        for c in s1:
            s[c] = s.get(c, 0) + 1
        
        w = {}
        l = 0

        for r, c in enumerate(s2):
            w[c] = w.get(c, 0) + 1
            while r - l + 1 > len(s1):
                w[s2[l]] -= 1
                if w[s2[l]] == 0:
                    del w[s2[l]]
                l += 1
            if s == w:
                return True
        return False