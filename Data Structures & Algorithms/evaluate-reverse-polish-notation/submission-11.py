import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }
        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                res = ops[t](a, b)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]