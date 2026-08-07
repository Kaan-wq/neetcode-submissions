from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s_info = sorted(zip(position, speed), key= lambda x: x[0], reverse=True)
        stack = deque()
        for (p, s) in s_info:
            if not stack: 
                stack.append((p, s))
                continue
            prev_p, prev_s = stack[-1]
            if (target - prev_p) / prev_s < (target - p) / s:
                stack.append((p, s))
        return len(stack)