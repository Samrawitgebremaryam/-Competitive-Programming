class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        l=0
        r = c*r -1 

        def finder (cell):
            i= cell // c
            j = cell % c
            return [i ,j]
        
        while l <= r :
            mid = (l+r)//2 
            val= finder (mid) 
            if target == matrix[val[0]][val[1]]:
                return True 
            elif target > matrix[val[0]][val[1]]:
                l = mid +1 
            else :
                r = mid - 1
        return False 
        



            

        # nums=[]
        # for i in range ( len ( matrix)):
        #     for j in range (len ( matrix[i])):
        #         nums.append(matrix[i][j])
        # print ( nums)
        # l,r = 0, len (nums)-1
        # while l <= r :
        #     mid = (l+r)//2 
        #     if target == nums[mid] :
        #         return True 
        #     elif target > nums[mid] :
        #         l = mid +1 
        #     else :
        #         r = mid + 1
        # return False 

