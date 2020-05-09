
# hashmap method - O(n) runtime/space
# make use of the fact : if sum(nums[i:j])==0, sums do not change between i,j. 
# use hashmap to store values and check if total-k is in a hashmap
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        total=0
        cnt=0
        dic={0:1}
        idx=0
        for i in range(n):
            total+=nums[i]
            if total-k in dic:
                cnt+= dic[total-k]
            dic[total] =dic.get(total, 0)+1
        print(dic)
        return cnt
                

#cumulative sum and without space method - time exceeded O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        total=0
        cnt=0
        for i in range(n):
            total=0
            for j in range(i,n):
                total+=nums[j]
                if total==k:
                    cnt+=1
        return cnt
