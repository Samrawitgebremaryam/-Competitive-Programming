class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=-1,len(nums)-1
        ans=[]
    
        while l+1 < r:
            mid = (l+r)//2
            if nums[mid]>=target:
                r = mid  
            else:
                l = mid
        first=r

        l,r=0,len(nums)
        while l + 1 < r:
            mid =(l+r)//2
            if nums[mid]<=target:
                l=mid
            else:
                r = mid  
        last=l
    
        if nums and nums[first] == target and nums[last] == target  :
            return [first,last ]
        else:
            return [-1,-1]


