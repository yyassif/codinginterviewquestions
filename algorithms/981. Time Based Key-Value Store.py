#44/45 cases passed time limit exceeded
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kv_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        print("set ", key,value, timestamp)
        if key in self.kv_map:
            self.kv_map[key][timestamp] = value
        else:
            self.kv_map[key] = {timestamp:value}

    def get(self, key: str, timestamp: int) -> str:
        print("get ", key, timestamp)
        prev_time=[]
        if key in self.kv_map:
            for time in self.kv_map[key]:
                if time==timestamp:
                    return self.kv_map[key][time]
                elif time>timestamp:
                    break
                if len(prev_time)==0 or time>prev_time[-1]:
                    prev_time.append(time)
            if len(prev_time)>0:
                return self.kv_map[key][prev_time[-1]]
            else:
                return ""
            
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
