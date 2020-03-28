#https://leetcode.com/problems/diet-plan-performance/discuss/373642/Python-sliding-window
def dietPlanPerformance(self, calories, k, lower, upper):
    points = 0
    total = sum(calories[0:k])
    if total < lower:
        points -= 1
    if total > upper:
        points += 1   
    i = 1
    while i+k-1 < len(calories):
        total = total - calories[i-1]+ calories[i+k-1]
        if total < lower:
            points -= 1
        if total > upper:
            points += 1
        i += 1
    return points

# brute force - time limit exceeded
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        score=0
        for i in range(n-k+1):
            sumv = 0
            sumv = sum(calories[i:i+k])
            if sumv<lower:
                score-=1
            elif sumv>upper:
                score+=1
        return score
