class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        perimeter=[]
        count=0
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2]:
                total=nums[i]+nums[i+1]+nums[i+2]
                perimeter.append(total)
                total=0
                count+=1
        if count==0:
            return 0
        else:
            return max(perimeter)
        