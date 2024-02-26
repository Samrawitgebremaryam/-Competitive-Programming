class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if n==1:
            return x 
        if n==-1:
            return 1/x 
            
        if n>0 and n%2==0:
            return self.myPow(x,n//2)**2
   
        elif n>0 and n%2==1:
            y=self.myPow(x,(n-1)//2)**2
            return x*y

        elif n<0 and n%2==0:
            return self.myPow(x,n//2)**2

        elif n<0 and n%2==1:
            y=self.myPow(x,(n-1)//2)**2
            return x*y 
        
            
