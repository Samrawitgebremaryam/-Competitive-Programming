class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        place=defaultdict(list) 
        result=[]

        for i in range(len(mat)):
            for j in range (len(mat[i])):
                place[i+j]+=[mat[i][j]]
        for key,values in place.items():
            if key%2==0:
                result.extend(values[::-1])
            else:
                result.extend(values)
        return result
                