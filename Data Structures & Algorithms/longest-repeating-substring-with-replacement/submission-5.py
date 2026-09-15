class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = {}
        left = 0
        best = 0
        max_freq = 0
        for right in range(len(s)):
            state[s[right]] = state.get(s[right], 0) + 1
            max_freq = max(state[s[right]], max_freq)

            while (right - left + 1) > max_freq + k:
                if state[s[left]] > 0:
                    state[s[left]] -= 1
                    left += 1
                else:
                    del state[s[left]]
            best = max(best, right - left + 1)
        return best