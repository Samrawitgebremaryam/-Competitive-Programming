class Solution:
    def totalMoney(self, n: int) -> int:
        if n<=7:
            return sum(range(1,n+1))
        start=1
        end=8
        monday=n//7
        reminder=n%7
        sums=0
        for _ in range (monday):
            sums+=sum(range(start , end ))
            start+=1
            end+=1
        for _ in range (reminder):
            sums+=start
            start+=1
        return sums





        