# brute force
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
