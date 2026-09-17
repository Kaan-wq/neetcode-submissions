from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        p_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in p_map.keys():
                if (not stack or stack.pop() != p_map[char]): return False
            else:
                stack.append(char)
        return len(stack) == 0