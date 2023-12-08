class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range (len(nums)):
            if nums[i]==i:
                continue
            else:
                return i
        else:
            return len(nums)
        