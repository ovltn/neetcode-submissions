class MinStack:

    def __init__(self):
        self.st = []
        self.prefix_min = []

    def push(self, val: int) -> None:
        self.st.append(val)

        if not self.prefix_min:
            self.prefix_min.append(val)
        else:
            self.prefix_min.append(min(self.prefix_min[-1], val))

    def pop(self) -> None:
        if not self.st:
            return

        self.st.pop()
        self.prefix_min.pop()

    def top(self) -> int:
        if not self.st:
            return None

        return self.st[-1]

    def getMin(self) -> int:
        if not self.prefix_min:
            return None

        return self.prefix_min[-1]