class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        l,r=0,1
        max_width=0
        while r<len(points):
            width=points[r][0]-points[l][0]
            max_width=max(max_width,width)
            l+=1
            r+=1
        return max_width


        