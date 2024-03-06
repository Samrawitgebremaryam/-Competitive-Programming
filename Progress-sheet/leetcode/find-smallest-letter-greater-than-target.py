class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r = -1 ,len(letters)-1  
        while l + 1 < r :
            mid = (l + r ) // 2
            if letters[mid] > target :
                r = mid 
            else: 
                l = mid 
        
        if r == len(letters)-1 and letters[r] <= target  :
            return letters [0]
        return letters [r]


        

            

        
        
        
        
        # l,r=0,len(letters)-1
        # mid =(l+r)//2
        # while l<=r:
        #     if nums[mid]==target:  
        #         return letters[mid+1]
        #     elif nums[mid] > target :
        #         r=mid-1
        #     else:
        #         l=mid+1  
        # if target > letters[mid]:
        #     return 
        # return letter[mid]
