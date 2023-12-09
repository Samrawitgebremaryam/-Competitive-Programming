class Solution(object):
    def pivotArray(self, nums, pivot):
        result =[]
        for i in range(len(nums)):
            if nums[i] < pivot:
                result.append(nums[i])
            if nums[i] == pivot:
                continue 
                
        x = nums.count(pivot)
        for _ in range(x):
            result.append(pivot)
   
        for j in range(len(nums)):
            if nums[j] > pivot:
                result.append(nums[j])
        return result
