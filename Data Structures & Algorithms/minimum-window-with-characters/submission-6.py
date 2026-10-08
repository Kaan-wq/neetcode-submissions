class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap, smap = {}, {}
        for c in t: tmap[c] = tmap.get(c, 0) + 1

        best = ""
        needed, ptr = len(tmap.keys()), 0
        for i, char in enumerate(s):
            smap[char] = smap.get(char, 0) + 1
            if char in tmap and smap[char] == tmap[char]:
                needed -= 1
            while needed == 0:
                if s[ptr] in tmap and smap[s[ptr]] == tmap[s[ptr]]:
                    best = s[ptr:i+1] if best == "" or i - ptr + 1 < len(best) else best
                    needed += 1
                smap[s[ptr]] -= 1
                ptr += 1
        return best