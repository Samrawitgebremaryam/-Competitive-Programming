class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        unique_numbers = set(nums)
        param = len(nums)//3
        res = []
        for num in unique_numbers:
            if nums.count(num)>param:
                res.append(num)
        return res
        