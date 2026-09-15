class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = {}
        left = 0
        best = 0
        max_freq = 0
        for right, char in enumerate(s):
            state[char] = state.get(char, 0) + 1
            max_freq = max(state[char], max_freq)
            while right - left + 1 > max_freq + k:
                state[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best