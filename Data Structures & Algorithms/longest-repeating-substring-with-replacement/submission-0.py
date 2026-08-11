from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        l = 0
        seen = defaultdict(int)
        for r in range(len(s)):
            seen[s[r]] += 1
            while r - l + 1 - max(seen.values()) > k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            best = max(best, r - l + 1)
        return best