class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        Even_sum=0
        result=[]
        for num in nums:
            if num%2==0:
                Even_sum+=num
        for query in queries:
            val,index=query
            if nums[index]%2==0:
                Even_sum-=nums[index]
            nums[index]+=val
            if nums[index]%2==0:
                Even_sum+=nums[index]
            result.append(Even_sum)
        return result
            
            














        

        