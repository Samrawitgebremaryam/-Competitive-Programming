class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:













        even_sum = 0
        answer = []
        for i in nums:
            even_sum+=i if i%2 == 0 else 0

        for query in queries:
            val,index = query
            if nums[index] %2 == 0:
                even_sum-=nums[index]
            nums[index]+=val
            if nums[index]%2 == 0:
                even_sum+=nums[index]
            answer.append(even_sum)
        return answer
            