class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        orginal=set(range(left,right+1) )
        covered=set()
        for range_ in ranges:
            for num in range(range_[0],range_[1]+1):
                if num in orginal :
                    covered.add(num)
        return covered==orginal
                

