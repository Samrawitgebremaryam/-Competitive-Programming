class Solution:
    def numberOfMatches(self, n: int) -> int:
        Games=0
        while(n>1):
            if n %2==1:
                Games+=((n-1)//2)
                n=((n-1)//2)+1
            else:
                Games+=(n//2)
                n=n//2
        return Games


        