from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map={}
        self.arr=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.arr:
            return False
        self.map[val] = len(self.arr) #store idx
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # DO NOT JUST DELETE FROM THE ARRAY
        if val in self.arr:
            idx = self.map[val]
            last = self.arr[-1]
            self.map[last] = idx
            self.arr[idx] = last
            del self.map[val]
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        #import random.choice!!
        return choice(self.arr)  #same as random.randint(0,len(self.arr)-1)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
