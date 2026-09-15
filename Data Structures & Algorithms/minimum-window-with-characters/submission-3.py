from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = Counter()
        missing = len(need)

        l = 0
        best_idx, best_len = 0, float("inf")

        for r, ch in enumerate(s):
            have[ch] += 1
            if have[ch] == need[ch]:
                missing -= 1

            while missing == 0:
                if r - l + 1 < best_len:
                    best_idx, best_len = l, r - l + 1

                out = s[l]
                have[out] -= 1
                if have[out] == need[out] - 1:
                    missing += 1
                l += 1

        return "" if best_len == float("inf") else s[best_idx:best_idx + best_len]