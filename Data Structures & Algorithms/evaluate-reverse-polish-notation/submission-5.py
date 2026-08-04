class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            if el in "+-*/" and len(el) == 1:
                b = stack.pop()
                a = stack.pop()
                if el == "+":
                    stack.append(a + b)
                elif el == "-":
                    stack.append(a - b)
                elif el == "*":
                    stack.append(a * b)
                else:
                    q = abs(a) // abs(b)
                    stack.append(q if (a < 0) == (b < 0) else -q)
            else:
                stack.append(int(el))
        return stack.pop()