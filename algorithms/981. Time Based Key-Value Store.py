#time O(1), space O(n)
import collections
import bisect
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if self.map.get(key, None) is None:
            return ""
        arr = self.map[key]
        #bisect returns idx after the value (point to insert)
        idx = bisect.bisect_left(arr,(timestamp,chr(127)))
        t,v = self.map[key][idx-1] #idx-1 b/c it's matched idx or before
        return v

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
