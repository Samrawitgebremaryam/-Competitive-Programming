class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result=0
      
        for i in range(len(points)-1):
            maxi=0
            for j in range(len(points[i])):
                diff=abs(points[i][j]-points[i+1][j])
                maxi=max(maxi,diff)
            result+=maxi
        return result 
          
        