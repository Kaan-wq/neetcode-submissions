from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info = zip(position, speed)
        s_info = sorted(info, key= lambda x: x[0], reverse=True)
        stack = deque()

        for (p, s) in s_info:
            if not stack: 
                stack.append((p, s))
                continue
            prev_p, prev_s = stack[-1]
            prev_time = (target - prev_p) / prev_s
            cur_time = (target - p) / s
            if prev_time < cur_time:
                stack.append((p, s))
        return len(stack)