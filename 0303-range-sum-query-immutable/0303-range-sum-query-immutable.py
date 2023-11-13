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
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)