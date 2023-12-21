class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        maximum=[0]*len(nums)
        maxi=nums[len(nums)-1]
        for i in range(len(nums)-1,-1,-1):
                maxi=max(maxi,nums[i]) 
                maximum[i]=maxi
        minimum=nums[0]
        for i in range(1,len(nums)-1):
            if nums[i]>minimum and nums[i]< maximum[i+1]:
                return True
            else:
                minimum=min(nums[i],minimum)
        return False
            
          
            




        # values={}
        # for i in range(len(nums)):
        #     values[nums[i]]=i
        # nums.sort()
        # for i in range(len(nums)-2):
        #     if nums[i]<nums[i+1]<nums[i+2] and values[nums[i]]<values[nums[i+1]]<values[nums[i+2]] :
        #         return True 
        # return False 
        

            

        

        