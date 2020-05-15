class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for path in paths:
            arr = path.split()
            direc = arr[0]
            for i in range(1, len(arr)):
                file = arr[i]
                open_p = file.index('(')
                close_p = file.index(')')
                content = file[open_p+1:close_p]
                filename = file[:open_p]
                if content in dic:
                    dic[content].append(direc+"/"+filename)
                else:
                    dic[content] = [direc+"/"+filename]
        res = []
        for key in dic:
            if len(dic[key])>1:
                res.append(dic[key])
        return res
