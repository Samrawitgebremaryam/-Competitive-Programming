class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort()
        nums=[0]*1000
        for i in range(len(trips)):
            nums[trips[i][1]]+=trips[i][0]
            if trips[i][2]<len(nums)-1:
                nums[trips[i][2]]-=trips[i][0]
        prefix=list(accumulate(nums))
        for i in range(len(prefix)):
            if prefix[i]>capacity:
                return False
        
        return True 
       
        