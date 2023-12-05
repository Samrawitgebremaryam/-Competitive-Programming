class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num/3)==math.ceil(num/3):
            x=num//3-1
            return [x,x+1,x+2]
        else:
            return []
            
        
        
        
        