#backtracking space/runtime O(3^N * 4^M) where N is the number of 3 letter numbers and M for 4 letter numbers
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        map= {"2":"abc","3":"def","4":"ghi", "5":"jkl","6":"mno", "7":"pqrs","8":"tuv", "9":"wxyz"}
        output=set()
        def backtrack(combi, next_digits):
            if len(next_digits)==0: #finished permutation. no more letters
                output.add(combi) #add finished string to output
            else:
                digit = next_digits[0]
                letters= map[digit]
                for i in range(len(letters)):
                    letter = map[digit][i:i+1]
                    backtrack(combi+letter, next_digits[1:])
        backtrack("", digits)
        return output
                    
                
