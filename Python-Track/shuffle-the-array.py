class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l,r=0,len(nums)//2
        result=[]
        while(r<len(nums)):
            result.append(nums[l])
            result.append(nums[r])
            l+=1
            r+=1
        return result 



        