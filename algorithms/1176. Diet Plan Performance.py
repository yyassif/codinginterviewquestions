#https://leetcode.com/problems/diet-plan-performance/discuss/373642/Python-sliding-window
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        score=0
        total =sum(calories[0:k])
        
        if total<lower:
            score-=1
        elif total>upper:
            score+=1
        print(total,score)
        for i in range(1,n-k+1):
            total = total-calories[i-1]+calories[i+k-1] #remove last value and add new value to the total
            if total<lower:
                score-=1
            elif total>upper:
                score+=1
            print(total, score, calories[i-1], calories[i+k-1])
        return score

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
