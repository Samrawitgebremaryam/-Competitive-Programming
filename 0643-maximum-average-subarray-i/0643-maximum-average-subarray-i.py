class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=sum(nums[:k])
        maxav=window/k
        for i in range(1,len(nums)-k+1):
            window-=nums[i-1]
            window+=nums[i+k-1]
            av=window/k
            maxav=max(maxav,av)
        return maxav









        # total = sum(nums[:k])
        # ori = total
        # i = 0
        # j = k
        # while j < len(nums):
        #     total -= nums[i]
        #     total += nums[j]
        #     if total > ori:
        #         ori = total
        #     i = i+1
        #     j = j+1
        # return ori/k