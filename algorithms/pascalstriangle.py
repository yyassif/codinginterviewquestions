class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        pas = []
        pas.append([1])
        for i in range(1,numRows): #starts at second row. first row [1] already appended.
            t = [1]
            for j in range(1,i+1):
                num=0
                try:
                    num += pas[i-1][j-1]
                except:
                    num+=0
                try:
                    num += pas[i-1][j]
                except:
                    num+=0
                t.append(num)
            pas.append(t)
        return pas
