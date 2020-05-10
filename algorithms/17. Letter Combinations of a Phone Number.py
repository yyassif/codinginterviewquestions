#backtracking space/runtime O(3^N * 4^M) where N is the number of 3 letter numbers and M for 4 letter numbers
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        dic= {"2":"abc","3":"def","4":"ghi", "5":"jkl","6":"mno", "7":"pqrs","8":"tuv", "9":"wxyz"}
        output=set()
        def backtrack(combi, digits):
            if len(digits)==0: #no more to permutate
                output.add(combi)
            else:
                letters = dic[digits[0]]
                for letter in letters:
                    backtrack(combi+letter, digits[1:])
        backtrack("", digits)  #combi=build letter combinations,
        return output
                
