class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        for i ,time  in count.items():
            if time>len(nums)//2:
                return i
       
        