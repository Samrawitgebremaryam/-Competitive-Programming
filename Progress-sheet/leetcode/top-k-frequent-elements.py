class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []  
        fre = Counter(nums) 

        fre_sorted = sorted(fre.items() , key = lambda x: x[1] , reverse = True)
        print (fre_sorted)
        for key,val in fre_sorted:

            if k == 0 :
                break 
            else:
                ans.append(key)
            k -= 1 
        return ans 


