class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = {}
        left = 0
        best = 0
        for right in range(len(s)):
            state[s[right]] = state.get(s[right], 0) + 1

            while sum(list(state.values())) > max(state.values()) + k:
                if state[s[left]] > 0:
                    state[s[left]] -= 1
                    left += 1
                else:
                    del state[s[left]]
            best = max(best, sum(list(state.values())))
        return best