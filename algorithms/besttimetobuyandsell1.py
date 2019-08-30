#Myungho Sim
#best time to buy and sell stock once
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        maxprofit=0
        min=sys.maxsize
        max=0
        for n in prices:
            if n<min:
                min = n
            elif n-min>maxprofit:
                maxprofit = n-min
        return maxprofit
