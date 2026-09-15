class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2: return False

        s1c, s2c = [0] * 26, [0] * 26
        ord_a = ord("a")
        for i in range(len_s1):
            s1c[ord(s1[i]) - ord_a] += 1
            s2c[ord(s2[i]) - ord_a] += 1

        m = 0
        for i in range(len(s1c)):
            m += 1 if s1c[i] == s2c[i] else 0
        
        l = 0
        for r in range(len_s1, len_s2):
            if m == 26: return True

            s2c[ord(s2[r]) - ord_a] += 1
            if s2c[ord(s2[r]) - ord_a] == s1c[ord(s2[r]) - ord_a]:
                m += 1
            elif s2c[ord(s2[r]) - ord_a] == s1c[ord(s2[r]) - ord_a] + 1:
                m -= 1
            
            s2c[ord(s2[l]) - ord_a] -= 1
            if s2c[ord(s2[l]) - ord_a] == s1c[ord(s2[l]) - ord_a]:
                m += 1
            elif s2c[ord(s2[l]) - ord_a] == s1c[ord(s2[l]) - ord_a] - 1:
                m -= 1
            l += 1

        return m == 26