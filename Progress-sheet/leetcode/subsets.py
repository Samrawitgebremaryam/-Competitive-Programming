class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        ans = []
        def find(index):
            ans.append(subset[:])
                
            for i in range (index,len(nums)):
                subset.append(nums[i])
                find( i+1)
                subset.pop()

        find( 0)
        return ans 
        