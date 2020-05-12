# run - O(S*N)  , space-O(n) S is the amount to change We use extra space for the memoization table.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        if n==0:
            return -1
        elif amount==0:
            return 0
        self.min_steps=float('inf')
        dic={}
        mini = float('inf')
        def rec(rem):
            if rem<0:
                return -1
            if rem==0:
                return 0
            if rem in dic and dic[rem]!=0:
                return dic[rem]
            mini = float('inf')
            for coin in coins:
                res = rec(rem-coin)
                if res>=0 and res<mini:
                    mini = res+1
                
            dic[rem] = mini if mini!=float('inf') else -1
            return dic[rem]
        return rec(amount)
