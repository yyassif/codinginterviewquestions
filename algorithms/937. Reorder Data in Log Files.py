#problem 937. Reorder Data in Log Files.py
#sol https://leetcode.com/problems/reorder-data-in-log-files/discuss/389466/Very-simple-Python-solution-using-sorted
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def order(x):
            arr = x.split(" ")
            is_digit = arr[1].isnumeric() #check if numbers after ID, isdigit() is ok
            if is_digit:
                return is_digit, [] # in case of numbers, return (True, a blank array), blank array=sort in the original order
            else: #chars come next
                #return False, rest of list after id and id
                return is_alpha, arr[1:], arr[0]  #ascending order sort=False comes first
        return sorted(logs, key=order)  

#####################################################################
#sol2 comentary sol- run- O(n log n) , space O(n) , n=total content of logs
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            id, rest = log.split(" ",1)
            return (0, rest, id) if rest[0].isalpha() else (1,) # (1,) because all digits are sorted in their original order
        return sorted(logs, key=f)
