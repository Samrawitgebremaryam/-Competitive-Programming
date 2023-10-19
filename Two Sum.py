class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list=[]
        for x in nums:
            for y in range(nums.index(x)+1,len(nums)):
                if x+nums[y]==target:
                    index_list.append(nums.index(x))
                    index_list.append(y) 
                    return index_list  
