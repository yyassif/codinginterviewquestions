#Myungho Sim
#judge if the robot starts at the origin and comes back to the orgin after following the path.
#from leetcode
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for s in moves:
            if s=="R":
                x+=1
            elif s=="L":
                x-=1
            elif s=="U":
                y+=1
            elif s=="D":
                y-=1
        if x==0 and y==0:
            return True
        elif x!=0 and y!=0:
            return False
                
            
