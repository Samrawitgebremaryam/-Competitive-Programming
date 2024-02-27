class Solution:
    def __init__(self):
        self.count={}

    def countGoodNumbers(self, n: int) -> int:
        if n==1:
            return 5
        if n==2:
            return 20
        if n not in self.count : 
            if n%2==1:
                self.count[n]=(self.countGoodNumbers(n//2)*self.countGoodNumbers(n//2+1))%(10**9+7)
            else :
                self.count[n]=( 4*self.countGoodNumbers(n-1))%(10**9+7)
        return self.count[n]

        

    
      