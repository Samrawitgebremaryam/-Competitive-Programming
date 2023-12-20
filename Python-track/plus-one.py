class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums=""
        result=[]
        nums="".join(map(str,digits))
        nums=str(int(nums)+1)
        result=list(map(int,nums))
        return result 
        

        