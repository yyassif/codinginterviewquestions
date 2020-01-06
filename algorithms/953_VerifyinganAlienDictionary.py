# 953. Verifying an Alien Dictionary on leetcode
# better than 93% efficiency and 100% of memory usage
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def checkOrder(a,b):
            size = (len(a)<len(b)) and len(a) or len(b)
            rs = True
            for i in range(size):
                index_a = order.index(a[i])
                index_b = order.index(b[i])
                #print(a[i],b[i],index_a,index_b)
                if index_a<index_b:
                    return rs
                elif index_a==index_b:
                    continue
                else:
                    rs=False
                    break
            if rs==True and len(a)>size:
                return False
            return rs #true if increasing order
        for i in range(len(words)-1):
            rs = checkOrder(words[i],words[i+1])
            if rs==False:
                break
        return rs
