class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1
                if count > 1:
                    return False
                
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True











# class Solution:
#     def checkPossibility(self, nums: List[int]) -> bool:
#         count=0
#         for i in range (len(nums)):
#            for j in range (i,len(nums)):
#                if nums[i]>=nums[j]:
#                     count+=1
#         if count>1:
#             return False
#         else: 
#             return True
          

        