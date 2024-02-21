class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cover =0
        count=i=0 
        while cover<n:
            if i<len(nums) and  nums[i] <= cover+1:
                cover += nums[i]   
                i+=1
            else:
                count += 1  
                cover += cover + 1
        return count 

        