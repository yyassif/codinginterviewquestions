'''
Sort based on timestamp
Create a dict and group sequences by user
For each user iterate ALL possible 3-sequence and use a dict to count each 3-sequence.
Track the most frequent 3-sequence and put them in a list. (Could be more than one most frequent 3-sequence)
Heapify that list and heappop once to get the result. (lexicographically smallest gurantee)
Time: O(n+nlogn+n^3), sort takes O(nlogn), iterate ALL possible 3-sequence takes O(n^3). iterate the sorted data takes O(n)
Space: O(n)
'''
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)): # sort based on timestamp
            data[u].append(w) # Group 3-sequence by user

        res, most, seq_dict = [], 0, {}
        for user, patterns in data.items():
            seq = self.helper(patterns)
            for s in seq:
                seq_dict[s] = seq_dict.get(s, 0) + 1
                if seq_dict[s] == most:
                    res.append(s)
                elif seq_dict[s] > most:
                    res = [s]
                    most = seq_dict[s]
        heapq.heapify(res)
        return heapq.heappop(res)
    
    def helper(self, lst):
		# Iterate ALL possible UNIQUE 3-sequence
        res = set()
        for l in range(len(lst)-2):
            for m in range(l+1, len(lst)-1):
                for r in range(m+1, len(lst)):
                    res.add((lst[l], lst[m], lst[r]))
        return res
