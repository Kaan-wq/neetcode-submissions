from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        letters = defaultdict(int)
        for letter in s:
            letters[letter] += 1
        
        for letter in t:
            if (letters[letter] == 0): return False
            letters[letter] -= 1
        return True
        