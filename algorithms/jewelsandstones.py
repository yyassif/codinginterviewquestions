#Myungho Sim
#better solution using hash map. 32ms sol better than 93% of submissions
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        map = {}
        cnt=0
        for s in S:
            try:
                val = map[s]
                val+=1
                map[s]=val
            except:
                map[s]=1
        for j in J:
            try:
                cnt+= map[j]
            except:
                cnt+=0
        return cnt

#brute force - better than 12% of submissions
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         sj = len(J)
#         ss = len(S)
#         cnt=0
#         for i in range(sj):
#             for j in range(ss):
#                 if J[i]==S[j]:
#                     cnt+=1
#         return cnt
