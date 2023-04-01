# Min Max Stack Construction

class Min_max_stack:
    def __init__(self) -> None:
        self.stack = []
        self.min_max_stack = []
    def push(self,val):
        new_min_max = {"min":val,"max":val}
        if len(Min_max_stack):
            old_min_max = self.min_max_stack[len(self.min_max_stack)-1]
            new_min_max["min"] = min(val,old_min_max["min"])
            new_min_max["max"] = max(val,old_min_max["max"])
        self.stack.append(val)
        self.min_max_stack.append(new_min_max)
    def pop(self):
        self.min_max_stack.pop()
        self.stack.pop()
    def peek(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[len(self.stack)-1]
    def get_min(self):
        if len(self.stack) == 0:
            return -1
        return self.min_max_stack[len(self.min_max_stack)-1]["min"]
    def get_max(self):
        if len(self.stack) == 0:
            return -1
        return self.min_max_stack[len(self.min_max_stack)-1]["max"]