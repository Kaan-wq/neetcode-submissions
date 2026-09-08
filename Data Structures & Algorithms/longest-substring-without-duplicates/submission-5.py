class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = {}
        left = 0
        best = 0
        for right in range(len(s)):
            while state.get(s[right], 0) > 0:
                state[s[left]] -= 1
                left += 1
            state[s[right]] = 1
            best = max(best, right - left + 1)
        return best