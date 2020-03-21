class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ret= []
        in_block=False
        for line in source:
            i=0
            if not in_block: #if not in block comment, such as multi line comment, create new newline array
                newline=[]
            while i<len(line):
                if line[i:i+2]=="/*" and not in_block: #begin block comment
                    in_block = True
                    i+=1
                elif line[i:i+2]=="*/" and in_block:  #close block comment
                    in_block = False
                    i+=1
                elif not in_block and line[i:i+2]=="//": #break if line comment within block comment
                    break
                elif not in_block:   #all else, if not in block comment, add line up to index i
                    newline.append(line[i])
                i+=1
            #combine result in case of multi-line block comment
            if newline and not in_block: 
                ret.append("".join(newline))
        return ret
