from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        p_map = {")": "(", "}": "{", "]": "["}
        p_in  = set(p_map.values())
        p_out = set(p_map.keys())
        for char in s:
            if char in p_in:
                stack.append(char)
            if char in p_out:
                if (not stack): return False
                if (stack.pop() != p_map[char]): return False
        return len(stack) == 0
