#problem 937. Reorder Data in Log Files.py
#sol https://leetcode.com/problems/reorder-data-in-log-files/discuss/389466/Very-simple-Python-solution-using-sorted
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def order(x):
            arr = x.split(" ")
            #sort :nums first. characters come next
            is_alpha = arr[1].isnumeric() #check if numbers after ID
            if is_alpha:
                return is_alpha, []
            else: #chars come next
                #return False, rest of list after id and id
                return is_alpha, arr[1:], arr[0] 
        return sorted(logs, key=order)
