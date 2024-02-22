class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans=0
        col=list(zip(*grid))
        print(col) 
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                ans+=(min(max(grid[i]),max(col[j])))-grid[i][j]

        return ans
