class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        pat=""
        pat_cnt=1
        pat_map = {}
        for s in pattern:
            if s in pat_map:
                pat+=str(pat_map[s])
            else:
                pat_map[s] = pat_cnt
                pat+=str(pat_cnt)
                pat_cnt+=1
        map = {}
        str_pat =""
        cnt=1
        for word in string.split():
            if word in map:
                str_pat +=str(map[word])
            else:
                map[word] = cnt
                str_pat +=str(cnt)
                cnt+=1
        return pat==str_pat
                
