#Myungho Sim
#best time to buy and sell stock 2
#idea taken from leetcode disucssion
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret =0
        size = len(prices)
        for i in range(size-1):
            if prices[i]<prices[i+1]:
                ret+=prices[i+1]-prices[i]
        return ret
