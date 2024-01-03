class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        once=0
        maxi=flips[0]
        for i in range(len(flips)):
            once+=1
            maxi=max(maxi,flips[i])
            if once==maxi:
                count+=1 
        return count



        # class Solution:
#     def numTimesAllBlue(self, flips: List[int]) -> int:
#         count = 0
#         nums = [0] * len(flips)
#         print (nums)
#         prefix_sum = 0
#         for i in range(len(flips)):
#             nums[flips[i] - 1] = 1
#             prefix_sum += nums[i]
#             if prefix_sum == i + 1:
#                 count += 1
#         return count

