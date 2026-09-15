from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        state_s, state_t = defaultdict(), defaultdict()
        for c in t:
            state_t[c] = state_t.get(c, 0) + 1
        m_obj = len(state_t.keys())

        l, m = 0, 0
        best_idx, best_len = 0, float("inf")
        for r in range(len(s)):
            state_s[s[r]] = state_s.get(s[r], 0) + 1
            if s[r] in state_t and state_s[s[r]] == state_t[s[r]]:
                m += 1
            while m == m_obj:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_idx = l
                state_s[s[l]] -= 1
                if s[l] in state_t and state_s[s[l]] + 1 == state_t[s[l]]:
                    m -= 1
                l += 1
        return "" if best_len == float("inf") else s[best_idx:best_idx + best_len]