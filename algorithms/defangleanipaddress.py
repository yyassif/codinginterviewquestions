#defangle IP address, easy problem @leetcode
#faster than 87%, less memory usage than 100% of submissions
class Solution:
    def defangIPaddr(self, address: str) -> str:
        size = len(address)
        last = 0
        string =""
        for i in range(size):
            if(address[i]=="."):
                string+= address[last:i]
                string+="[.]"
                last = i+1
        string+=address[last:size]
        return string
    
#faster than 64%, less memory usage than 100% of submissions
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace(".","[.]")
