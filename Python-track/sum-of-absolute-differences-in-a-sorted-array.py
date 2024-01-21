class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total=sum(nums)
 
        prefix=0
        ans=[]
    
        for i in range (len (nums)):
            prefix+=nums[i]
            ans .append((((i+1)*nums[i])-prefix)+((total-prefix)-(nums[i]*(len(nums)-i-1)))) 
  
        return ans
    

        
            
                   