class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i=0
        while i<n-1:
            if chars[i]==chars[i+1]:
                idx=i
                cnt=1
                while idx<n-1 and chars[idx]==chars[idx+1]:
                    idx+=1
                    cnt+=1
                for j in range(cnt-1):
                    del chars[i+1]
                idx=i
                i+=1
                # print(chars,cnt,idx)
                cnt_digit=0
                cnt_copy = cnt
                while cnt>0:
                    chars.insert(idx+1,str(cnt%10))
                    cnt=cnt//10
                    i+=1
                    cnt_digit+=1
                n=n-cnt_copy+cnt_digit+1
            else:
                i+=1
        return len(chars)
                
