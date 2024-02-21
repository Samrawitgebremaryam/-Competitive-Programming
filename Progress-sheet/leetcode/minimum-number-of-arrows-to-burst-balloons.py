class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        ans=1
        end=points[0][1]
        for r in range (1,len (points)):
            if points [r][0]<=end:
                end=min(end,points[r][1])
            else:
                
                ans+=1
                end=points[r][1]
        return ans 






        # l=ans=0 
        # for r in range (1,len (points)):
        #     if points[l][1]<points[r][0]:
        #         ans+=1 
        #         l=r
        # return ans 


