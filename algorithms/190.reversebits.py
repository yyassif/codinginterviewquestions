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
