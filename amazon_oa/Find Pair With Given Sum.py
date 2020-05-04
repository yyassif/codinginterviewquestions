class Solution():
    def FindPair(self, nums, target):
        assert isinstance(nums, list)
        assert isinstance(target, int)

        if nums is None:
            return None

        target = target - 30
        dic = {}
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in dic:
                ans.append([dic[target - nums[i]], i])
            dic[nums[i]] = i
        return max(ans)
    

#####################################################
#sol 2
nums = [20, 50, 40, 25, 30, 10]
target = 90-30

map ={}
x=0 #x is bigger number in the pair
y=0 #y is smaller number in the pair
for i,num in enumerate(nums):
    diff = target-num
    if diff in map:
        if x==0 and y==0:
            if num<diff:
                x= diff
                y= num
            else:  
                x= num
                y= diff
        else:
            if num<diff:
                if x<diff:
                    x= diff
                    y= num
            else:
                if x<num:  
                    x= num
                    y= diff
print(num, diff)
