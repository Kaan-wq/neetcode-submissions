class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            d = s.find("#", i)
            l = int(s[i:d])
            i = d + 1 + l
            strs.append(s[i-l: i])
        return strs