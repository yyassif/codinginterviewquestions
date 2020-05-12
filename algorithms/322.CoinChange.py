# 322. Coin Change
# bottom up dp sol adapted from: good sol https://leetcode.com/problems/coin-change/discuss/509722/python.-easy-DP-solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [amount+1 for i in range(amount+1)] # most you can do is N times by using "1" coin.
        arr[0] = 0
        for i in range(1, amount+1):
            mini = arr[i]
            for coin in coins:
                if i-coin>=0:
                    mini = min(mini, arr[i-coin]+1)
            arr[i] = mini
        if arr[-1]>amount:
            return -1
        return arr[amount]
############################################################################################################
# run - O(S*N)  , space-O(n) S is the amount to change We use extra space for the memoization table.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        if n==0:
            return -1
        elif amount==0:
            return 0
        self.min_steps=float('inf')
        dic={}  #key=remainder(amount-coin), value=min_steps
        mini = float('inf')
        def rec(rem):
            if rem<0:
                return -1
            if rem==0:
                return 0
            if rem in dic and dic[rem]!=0: #if rem=amount-coin value already explored
                return dic[rem] #min_steps so far
            mini = float('inf')
            for coin in coins:
                res = rec(rem-coin)  #res=min step
                #update mini=min_step
                if res>=0 and res<mini:  #recursive call return value is 0 or greater - amount found or being searched
                    mini = res+1
                
            dic[rem] = mini if mini!=float('inf') else -1
            return dic[rem]
        return rec(amount)
