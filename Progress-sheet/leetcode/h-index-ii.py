class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l,r = 0 , len(citations)-1
        while l <= r: 
            mid = (l+r)//2 
            if citations[mid] == (len(citations) - mid ):
                return citations[mid]
            elif citations[mid] < (len(citations) - mid ):
                l = mid +1 
            else:
                r = mid - 1
        return len(citations) - l

        









        # l, r = -1 , len(citations) -1
        # def count (middle):
        #     count=0  

        #     for i in range (middle , len(citations)):
        #         if citations[i] >= citations[middle] :
        #             count +=1 
        #     return count 

        # if len(citations) == 1 :
        #     if citations[0] == 0 :
        #         return 0
        #     return 1 

        # if sum (citations) == 0:
        #     return 0

        # if len(citations) == 2:
        #     if citations[0] == 0  and citations[1] == 1 :
        #         return 1
            
        # while l +1 < r :
        #     mid = (l+r)//2
        #     val= count(mid)
        #     if val >= mid :
        #         l = mid 
        #     else:
        #         r = mid 
        # return l


