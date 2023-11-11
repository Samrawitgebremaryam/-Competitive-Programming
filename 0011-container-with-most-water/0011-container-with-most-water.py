class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        l,r=0,len(height)-1
        while l<r:
            area=min(height[l],height[r])*(r-l)
            max_area=max(max_area,area)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return max_area



   
   
   
   
   
   
    #    maxvolume= 0
    #     l=0
    #     r=len(height)-1
        
    #     while l<r:
    #         hleft = height[l]
    #         hright = height[r]
    #         minimum = min(hleft, hright)
    #         diff = r - l
    #         volume_curr = minimum * diff
    #         maxvolume= max(maxvolume, volume_curr)
            
    #         if height[l]<height[r]:
    #             l+=1
    #         else:
    #             r-=1
    #     else:
    #         return maxvolume
                