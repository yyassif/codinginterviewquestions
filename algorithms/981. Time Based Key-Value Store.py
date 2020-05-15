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
        #bisect returns idx after the value (point to insert) since chr(127) bigger than all chars
        i = bisect.bisect(arr,(timestamp,chr(127)))
        #idx-1 b/c it's matched idx or before
        return arr[i-1][1] if i else "" #if i returns 0, return ""

# i = bisect.bisect(a,b) will set i to the first index where a[i] > b
# for this case- a is our list of tuples and b is our target tuple
# to correctly define the target we must provide a tuple following format (number, string).
# number is timestamp. string we must use a value > any provided string.
# i.e. 'z' > 'yyyyy', therefore 'z'+1 must be greater than any 'a-z' string.
# chr( ord('z')+1 ) = chr(123)
# chr(127) can also be used to include all valid ascii characters(7 bits 0-127)
