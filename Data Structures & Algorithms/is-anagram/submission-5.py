class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        shash, thash = {}, {}

        for (a, b) in zip(s, t):
            shash[a] = shash.get(a, 0) + 1
            thash[b] = thash.get(b, 0) + 1
        
        return shash == thash