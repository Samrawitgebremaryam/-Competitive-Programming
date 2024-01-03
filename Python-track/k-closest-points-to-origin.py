class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        points.sort(key=lambda x:(x[0]**2)+(x[1]**2))
        print(points)
        for i in range(k):
            ans .append(points[i])
        return ans 

        
         