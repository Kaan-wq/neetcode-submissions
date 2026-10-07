class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_sum = best = ptr = 0
        char_map = {}

        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
            char_sum += 1
            while char_sum > k + max(char_map.values()):
                char_map[s[ptr]] -= 1
                char_sum -= 1
                if char_map[s[ptr]] == 0:
                    del char_map[s[ptr]]
                ptr += 1
            best = max(best, char_sum)
        return best