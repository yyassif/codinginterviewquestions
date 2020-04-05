def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def getKeys(x):
            k = x.split(" ")
            l = k[1].isdigit()
            if l:
                return l, []
            else:
                return l, k[1:], k[0]
        
        return sorted(logs, key=getKeys)
