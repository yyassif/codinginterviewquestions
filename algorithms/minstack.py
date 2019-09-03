#Myungho Sim
#min stack implementation. problem from leetcode
#faster than 90% of submissions
import sys
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min =[]    
        self.arr = []   
    def push(self, x: int) -> None:
        self.arr.append(x)
        if not self.min or x<=self.min[-1]:
            self.min.append(x)
        
    def pop(self) -> None:
        lastElement = self.arr[-1]
        del self.arr[-1]
        #update min
        if lastElement==self.min[-1]:
            del self.min[-1]

    def top(self) -> int:
        lastIdx = len(self.arr)
        return self.arr[lastIdx-1]

    def getMin(self) -> int:
        if len(self.min)>0:
            return self.min[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
