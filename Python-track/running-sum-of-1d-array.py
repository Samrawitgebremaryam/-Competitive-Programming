class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum=[]
        total=0
        for i in range (len(nums)):
            total+=nums[i]
            prefix_sum.append(total)
        return prefix_sum 