class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
     
        nums.sort()
        min_distance=float("inf")
        for i in range(len(nums)-2):
            l, r = i+1,len(nums)-1

            while l<r: 
                if nums[l]+nums[r]+nums[i] ==target:
                    return target 
                if nums[l]+nums[r] + nums[i]< target:
                    distance=abs(target-(nums[l]+nums[r]+nums[i]))
                    
                    if distance < min_distance:
                        min_distance=distance
                        summ=nums[l]+nums[r]+nums[i]
                    l+=1 
                else: 
                    distance=abs(target-(nums[l]+nums[r]+nums[i]))
                    if distance < min_distance:
                        min_distance=distance
                        summ=nums[l]+nums[r]+nums[i]
                    r-=1
        return summ

            


        
        