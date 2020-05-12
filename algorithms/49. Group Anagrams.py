class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for string in strs:
            temp= ''.join(sorted(string))
            if temp in dic:
                dic[temp].append(string)
            else:
                dic[temp] = [string]
        ret=[]
        for key in dic:
            ret.append(dic[key])
        return ret
