#sol 1 https://leetcode.com/problems/reverse-bits/discuss/532029/Python-or-One-line-Solution
def reverseBits(n):
			return int('{0:032b}'.format(n)[::-1],2)
