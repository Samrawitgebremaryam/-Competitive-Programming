class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def subset(index,path):
            if index>=len(nums):
                ans.append (path[:])
                return 

            path.append(nums[index])
            subset(index+1,path)
            path.pop()

           
            while index+1 < len(nums) and nums[index] == nums[index+1] :
                index+=1
            subset(index+1,path)
        ans=[]
        subset (0,[])
        return ans              