class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        mat=[]
        for i in range (len (matrix)):
            new=[]
            for j in range (len (matrix[i])):
                new.append(matrix[j][i])
            mat.append(new[::-1]) 

        for i in range (len(mat)):
            for j in range (len(mat[i])):
                matrix[i][j]=mat[i][j]
        """
        Do not return anything, modify matrix in-place instead.
        """
        