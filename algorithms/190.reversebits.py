#190 reverse bits
#referenced from https://leetcode.com/problems/reverse-bits/discuss/54792/one-line-python-solution-with-brief-explanation
# '{0:032b}'.format(n)
# The first '0' - format the 0th(the first) argument; 
# the second '0'- for padding
# '32' - total length of the output
# 'b' - binary.
class Solution:
  def reverseBits(self, n):
    return int('{0:032b}'.format(n)[::-1], 2)

#sol 2 https://leetcode.com/problems/reverse-bits/discuss/531594/Python-3-lines-solution
n_str = bin(n)[2:]
n_str = n_str.zfill(32)
return int(n_str[::-1],2)

#bit manipulation method https://leetcode.com/problems/reverse-bits/discuss/271179/Python-Solution-Bit-Manipulation
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s=""
        for i in range(32):
            s=s+str(n>>i & 1)
        return int(s,2)
