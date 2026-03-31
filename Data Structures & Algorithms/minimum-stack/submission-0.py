class MinStack:

    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        self.values.append(val)

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        tmp = []
        lowest = self.values[0]

        while len(self.values):
            lowest = min(lowest, self.values[-1])
            tmp.append(self.values.pop())

        while len(tmp):
            self.values.append(tmp.pop())
        
        return lowest


