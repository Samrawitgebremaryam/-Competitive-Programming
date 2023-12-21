class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans=0
        
        for i in range (1,len(grid)-1):
            total=0
            for j in range(1,len(grid[i])-1):
                total=grid[i][j]+grid[i-1][j]+grid[i-1][j+1]+grid[i+1][j]+grid[i-1][j-1]+grid[i+1][j-1]+grid[i+1][j+1] 
                ans=max(ans,total)
        return ans









        # value=0
        # for i in range(0,3,2):
        #     for j in range(0,3):
        #         value+=grid[i][j]
        # value+=grid[1][1]
        # return value  



        