#lru cache
#tip on ordereddict https://www.journaldev.com/21807/python-ordereddict
# ** OrderedDict popitem : removes the items in FIFO order.
# It accepts a boolean argument **last**, if it’s set to True then items are returned in LIFO order.
# We can move an item to the beginning or end of the OrderedDict using move_to_end function.
# It accepts a boolean argument last, if it’s set to False then item is moved to the start of the ordered dict.
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
