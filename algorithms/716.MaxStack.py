#Myungho Sim
#716 max stack leet code problem
# solution using stacks. 60% better runtime, 100% better memory
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack:
            m = self.stack[-1][1]
            m = max(m,x)
        else:
            m =x
        self.stack.append((x,m))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        m = self.stack[-1][1]
        temp =[]
        while self.stack[-1][0]!=m:
            temp.append(self.stack.pop()[0])
        self.stack.pop()
        while temp:
            self.push(temp.pop())
        return m


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
