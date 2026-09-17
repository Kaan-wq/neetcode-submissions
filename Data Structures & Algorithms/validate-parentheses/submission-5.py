class Solution:
    def isValid(self, s: str) -> bool:
        dq = collections.deque()
        p_map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in p_map.keys():
                if (not dq or dq.pop() != p_map[char]): return False
            else:
                dq.append(char)
        return len(dq) == 0