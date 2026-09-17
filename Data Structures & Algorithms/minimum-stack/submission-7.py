class MinStack:
    def __init__(self):
        self.stack_min = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack_min:
            self.stack_min.append(val)
        else:
            if self.stack_min[-1] >= val:
                self.stack_min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        p_val = self.stack.pop()
        if self.stack_min and self.stack_min[-1] == p_val:
            self.stack_min.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1] if self.stack_min else 2^31 - 1