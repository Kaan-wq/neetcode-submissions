import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                res = int(ops[t](a, b))
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]