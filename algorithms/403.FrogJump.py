#403. Frog Jump
#DFS sol adapted from https://leetcode.com/problems/frog-jump/discuss/418003/11-line-DFS-solution
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        visited = set()
        def jump(val, step):
            if (val+step) not in stones or ((val, step) in visited):
                return False
            if val+step==stones[-1]:
                return True
            visited.add((val,step))
            return jump(val+step,step-1) or jump(val+step, step) or jump(val+step, step+1)
        return jump(stones[0], 1)
