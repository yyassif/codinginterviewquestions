#303.rangesumquery.py
class NumArray:
    def __init__(self, nums: List[int]):
        self.arr = nums
        for i in range(1,len(nums)):
            self.arr[i] +=self.arr[i-1]

    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.arr[j]
        else:
            return self.arr[j]-self.arr[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
