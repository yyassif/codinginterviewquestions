# 225. Implement Stack using Queues
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr =[]
        self.size=0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.arr.append(x)
        self.size+=1
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        popped = self.arr[self.size-1]
        del self.arr[self.size-1]
        self.size-=1
        return popped

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.arr[self.size-1]        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
