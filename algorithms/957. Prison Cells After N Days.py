#https://leetcode.com/problems/prison-cells-after-n-days/discuss/534042/Python-3-Find-loop-and-Mod-O(2**N)
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cur, first_day, count = [0]*8, None, 0
        while N:
            for c in range(1,7):
                if cells[c-1] == cells[c+1]:
                    cur[c] = 1
                else:
                    cur[c] = 0
                    
            if count == 0: #copy first day 
                first_day = cur[:]
            elif cur == first_day: 
                N %= count
            
            cells = cur[:]
            count += 1
            N -= 1
        return cur
