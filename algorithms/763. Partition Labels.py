# 763. Partition Labels
# greedy sol - time complexity - O(n)
# space complexity O(n)=O(1) because input only consist of a to z, only extra space for mapping 26 letters
#e.g. "ababcbacadefegdehijhklij" ->"ababcbaca", "defegde", "hijhklij" ->Output: [9,7,8]
# watch where a is. idx where a last occurs is m['a']=9. the last idx for b, c is before last of a. 
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
