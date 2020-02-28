#166. Fraction to Recurring Decimal
#sol adapted from leetcode
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        frac=""
        if numerator<0 ^ denominator<0:
            frac+="-"
        dividend = abs(numerator)  # it can be negative numbers
        divisor = abs(denominator)
        frac+=str(dividend//divisor)
        remainder= numerator%denominator
        if remainder==0:
            return frac
        frac+="."
        map={}
        while(remainder!=0):
            if remainder in map:
                idx=map[remainder]
                frac = frac[:idx]+"("+frac[idx:]+")"
                return frac
            map[remainder] = len(frac)
            remainder*=10
            frac+= str(remainder//divisor)
            remainder%=divisor    # e.g. 670%333 = 4
        return frac
