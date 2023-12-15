class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        covered=set()
        numbers=set(nums)
        maxi=0
        for num in nums:
            count=0
            n=num
            if num not in covered:
                while (num+1 in numbers):
                    count+=1 
                    num+=1
                    covered.add(num)
        
                while (n-1 in numbers):
                    count+=1
                    n-=1
                    covered.add(n)
                    
                maxi=max(count+1,maxi)
        return maxi
        