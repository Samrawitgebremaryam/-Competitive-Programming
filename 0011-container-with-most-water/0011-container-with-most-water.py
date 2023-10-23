class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxvolume= 0
        l=0
        r=len(height)-1
        
        while l<r:
            hleft = height[l]
            hright = height[r]
            minimum = min(hleft, hright)
            diff = r - l
            volume_curr = minimum * diff
            maxvolume= max(maxvolume, volume_curr)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        else:
            return maxvolume
                
            
        