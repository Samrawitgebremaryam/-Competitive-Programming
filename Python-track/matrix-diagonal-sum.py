class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result=0
        for i in range (len(mat)):
            for j in range (len(mat[i])):
                if i==j or i+j==len(mat[i])-1:
                    result+=mat[i][j] 
        return result
            
        