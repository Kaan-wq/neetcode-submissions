from collections import defaultdict

class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            n = int(s[i:j])
            strs.append(s[j + 1 : j + 1 + n])
            i = j + 1 + n
        return strs
        