class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        post=[] 
        product=1
        for i in range(len(nums)):
            product*=nums[i]
            pre.append(product) 
        product=1
        for i in range (len(nums)-1,-1,-1):
            product*=nums[i]
            post.append(product)
        post.reverse()

        result=[post[1]]
        for i in range(1, len(nums)):
            if i==len(nums)-1:
                result.append(pre[i-1])
            else:
                result.append(post[i+1]*pre[i-1])
        return result
        

        