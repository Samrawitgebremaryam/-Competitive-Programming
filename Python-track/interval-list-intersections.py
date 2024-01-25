class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l,r=0,0
        ans = []
        while l < len(firstList) and r < len(secondList):
            first = firstList[l]
            second = secondList[r]
            if not (second[1] < first[0] or second[0] > first[1]):   
                ans.append([max(second[0], first[0]), min(second[1], first[1])])
            if first[1] < second[1]:
                l += 1
            else:
                r += 1
        return ans
        
            
            
        