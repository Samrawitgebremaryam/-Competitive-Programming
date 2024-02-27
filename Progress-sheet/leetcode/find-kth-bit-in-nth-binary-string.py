class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return "0"
        if n!=1 and  k == ceil(((2**n)-1)/2):
            return "1"
        elif n != 1 and k < ceil((2**n-1)/2):
            return self.findKthBit(n-1,k)
        elif k > ceil(((2**n)-1)/2):
            k=(2**n-1)-k+1
            parent=self.findKthBit(n-1,k)
            return str(int(parent)^1)

        
         
        
        
        
        


        