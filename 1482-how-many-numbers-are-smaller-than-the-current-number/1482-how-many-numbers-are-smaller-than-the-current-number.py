class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        values=[]
        for i in range(len(nums)):
            flag=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    flag+=1 
            values.append(flag)
            
        return values
        

