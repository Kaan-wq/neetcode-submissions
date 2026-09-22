class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0])
        stack = []
        for p, s in cars:
            if not stack:
                stack.append((p, s))
                continue
            prev_p, prev_s = stack[-1]
            while (target - p) / s >= (target - prev_p) / prev_s:
                stack.pop()
                if stack:
                    prev_p, prev_s = stack[-1]
                else:
                    break
            stack.append((p, s))
        return len(stack)