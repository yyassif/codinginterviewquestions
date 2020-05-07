#cleaner sol https://leetcode.com/problems/string-to-integer-atoi/discuss/519546/Python-or-Very-Simple-and-StraightForward
class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        sign = 1
        num = 0

        while i < len(str) and str[i] == ' ':
            i += 1

        # step 2: +/- sign
        if i < len(str):
            if str[i] == '+':
                i += 1
            elif str[i] == '-':
                sign = -1
                i += 1

        # step 3: integral
        while i < len(str):
            if str[i].isdigit():
                num *= 10
                num += int(str[i])
                i += 1
            else:
                break

        # step 4: check larger than max
        if sign == 1 and num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif sign == -1 and num > 2 ** 31:
            return -2 ** 31
        else:
            return sign * num
        
##############################################################
#my sol
#for loop and many if stmts 
class Solution:
    def myAtoi(self, str: str) -> int:
        num=0
        is_neg=False
        is_pos=False
        non_space=False
        neg=1
        map ={"1":1,"2":2,"3":3,"4":4,"5":5, "6":6, "7":7, "8":8,"9":9,"0":0}
        num_found=False
        for d in str:
            print("d",d)
            # if num_found==False and d.isalpha() and d!="-" and d!="+":
            #     break
            if d=="+":
                if num_found==True:
                    break
                if is_pos==True or is_neg==True:
                    break
                if is_neg==True or num_found==True:
                    return 0
                is_pos=True
            elif d=="-" :
                if num_found==True:
                    break
                if is_neg==True or is_pos==True:
                    break
                if is_pos==True or num_found==True or is_neg==True:
                    return 0
                else:
                    is_neg=True
            elif d==".":
                if num_found==True:
                    break
                else:
                    return 0
            elif d.isdigit():
                num_found=True
                neg=-1 if is_neg==True else 1
                print(neg*num*10+map[d])
                if (num*10+map[d])>2**31 and neg==-1:
                    return -2**31
                elif neg*num*10+map[d]>2**31-1:
                    return 2**31-1
                else:
                    num = num*10+map[d]
            elif d==' ' and non_space==False:
                continue
            elif d==' ' and non_space==True:
                break
            else:
                break
            if d!=' ':
                non_space=True
        return num*neg
