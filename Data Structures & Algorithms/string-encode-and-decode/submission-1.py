class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            if s[i] == "#":
                length = int(s[0:i])
                decoded.append(s[i+1:i+length+1])
                i += length + 1
                s = s[i:]
                i = 0
            i += 1
        return decoded