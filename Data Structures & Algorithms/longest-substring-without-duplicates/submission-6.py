class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128
        left = 0
        best = 0
        for right, ch in enumerate(s.encode()):
            p = last[ch]
            if p >= left:
                if right - left > best:
                    best = right - left
                left = p + 1
            last[ch] = right
        return max(best, len(s) - left)