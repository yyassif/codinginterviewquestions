# 763. Partition Labels
# greedy sol - space and time complexity - O(n)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        m = {c:i for i,c in enumerate(S)}
        ret = []
        j,anchor=0,0
        for i,c in enumerate(S):
            j=max(j, m[c]) #check max idx of the label
            if i==j: #at the end of the current partition
                ret.append(i-anchor+1)
                anchor=i+1 #move anchor to the start of the next partition
        return ret
