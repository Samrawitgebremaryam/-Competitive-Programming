class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        else:
            pick =0
            index=0

            for i in range (len(arr)):
                if arr[i]>pick:
                    pick=arr[i]
                    index=i
            if index ==len(arr)-1 or index==0:
                return False
            
            for i in range (index,len(arr)-1):
                if arr[i]<=arr[i+1]:
                    return False
            for i in range (0,index):
                if arr[i]>=arr[i+1]:
                    return False
        return True 
        
            




