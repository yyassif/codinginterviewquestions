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

#analysis https://leetcode.com/articles/frog-jump/
# Time complexity : O(3^n) Recursion tree can grow upto 3^n
# Space complexity : O(n) Recursion of depth n is used.


# Python BFS DP without recursion
# https://leetcode.com/problems/frog-jump/discuss/88900/Python-BFS-DP-without-recursion

class Solution(object):
def canCross(self, stones):
    steps={key:[] for key in stones}
    steps[0].append(0)
    for i in xrange(len(stones)):
        for j in steps[stones[i]]:
            for jump in (j-1,j,j+1):
                nxt = stones[i]+jump
                if nxt==stones[-1]:
                    return True
                if nxt in steps and (not steps[nxt] or steps[nxt][-1]>jump):
                    steps[nxt].append(jump)
    return False
