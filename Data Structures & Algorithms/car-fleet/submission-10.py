class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        stack = []
        for p, s in cars:
            t_curr = (target - p) / s
            if stack and t_curr <= stack[-1]:
                continue
            stack.append(t_curr)
        return len(stack)