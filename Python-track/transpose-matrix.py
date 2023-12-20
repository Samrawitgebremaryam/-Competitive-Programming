class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        new=[]
        for i in range (len(matrix[0])):
            for j in range(len(matrix)):
                new.append(matrix[j][i])
            result.append(new)
            new = []
        return result

        