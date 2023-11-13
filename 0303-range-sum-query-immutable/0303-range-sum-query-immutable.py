class NumArray:
    def __init__(self, nums: List[int]):
            self.prefixSum=[0]
            curr=0
            for i in range(len(nums)):
                curr+=nums[i]
                self.prefixSum.append(curr)
    def sumRange(self, left: int, right: int) -> int:
        leftSum=self.prefixSum[left]
        rightSum=self.prefixSum[right+1]
        return rightSum-leftSum


# def __init__(self, nums: List[int]):
#             self.prefixsum=[0]
#             for i in nums:
#                 self.prefixsum.append(self.prefixsum[-1]+i)
#     def sumRange(self, left: int, right: int) -> int:
#         return  self.prefixsum[right+1]- self.prefixsum[left]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)