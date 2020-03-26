#https://leetcode.com/problems/prison-cells-after-n-days/discuss/534042/Python-3-Find-loop-and-Mod-O(2**N)
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        output, first_day, count = [0]*8, None, 0
        while N:
            for c in range(1,7):
                if cells[c-1] == cells[c+1]:
                    output[c] = 1
                else:
                    output[c] = 0
                    
            if count == 0: #copy ouput to detect cycles
                first_day = output[:]
            elif output == first_day: #if cycle detected, only run remaining
                N %= count
            
            cells = output[:]
            count += 1
            N -= 1
        return output
