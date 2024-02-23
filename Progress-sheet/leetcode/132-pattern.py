class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        left=[]
        mini=inf
        stack=[]
        for i in range (len(nums)):
            left.append(mini)
            mini=min(mini,nums[i])
        
        for i in range (len (nums)-1,-1,-1):
            while stack and nums[i] > stack[-1]:
                right=stack.pop()

                if right>left[i]:
                    return True 
            stack.append(nums[i])

        return False 
