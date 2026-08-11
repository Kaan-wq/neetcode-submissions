from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1
        
        w_map = defaultdict(int)
        have = 0
        l = 0
        best_len, best_start = 1e7, 0

        for r in range(len(s)):
            w_map[s[r]] += 1
            if s[r] in t_map and t_map[s[r]] == w_map[s[r]]:
                have += 1
            while have == len(t_map):
                if r - l + 1 < best_len:
                    best_len, best_start = r - l + 1, l
                if s[l] in t_map and t_map[s[l]] == w_map[s[l]]:
                    have -= 1
                w_map[s[l]] -= 1
                l += 1
        return s[best_start:best_start + best_len] if best_len != 1e7 else ""