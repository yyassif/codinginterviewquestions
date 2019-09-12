#Myungho Sim
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.arr = nums.copy()
        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ret = self.arr.copy()
        random.shuffle(ret)
        return ret
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
#also review a different sol from leetcode
#https://leetcode.com/problems/shuffle-an-array/discuss/349369/Python%3A-why-not-inherit-from-list
